"""
BasketShield AI - Core Operations Research Optimizer (Google OR-Tools)
Mixed-Integer Linear Programming (MILP) solving multi-supplier allocation,
Big-M semi-continuous MOQ gating, capacity, certified recycling targets, and lead-time constraints.
"""

from ortools.linear_solver import pywraplp
import pandas as pd
import numpy as np

def compute_supplier_landed_cost(supplier, macro_shock, can_metal_mass_kg=0.013, cans_per_feu=130000):
    """
    Computes exact physical landed cost per unit for a packaging converter.
    C_s = Metal_Term + Conversion_Term + Tariff_Term + Freight_Term
    """
    lme = macro_shock["lme_aluminum_usd_per_tonne"]
    premium = macro_shock["us_midwest_premium_usd_per_tonne"]
    tariff_pct = macro_shock["section_232_tariff_pct"] if supplier["section_232_tariff_applies"] else 0.0
    container_rate = macro_shock["ocean_container_feu_usd"]
    
    # Metal cost per kg = (LME + Premium) / 1000
    metal_cost_per_kg = (lme + premium) / 1000.0
    
    # Primary vs recycled discount factor:
    # Recycled scrap prices track ~75-80% of LME cash, saving energy surcharges
    primary_ratio = supplier["primary_metal_exposure"]
    effective_metal_cost_per_kg = metal_cost_per_kg * (primary_ratio + (1.0 - primary_ratio) * 0.78)
    
    # Metal cost per can
    metal_cost_per_unit = can_metal_mass_kg * effective_metal_cost_per_kg
    
    # Conversion cost
    conversion_cost = supplier["base_conversion_cost_usd"]
    
    # Tariffs (applied on imported metal value if Section 232 applies)
    tariff_cost = metal_cost_per_unit * (tariff_pct / 100.0)
    
    # Freight cost per can:
    # If supplier is overseas, ocean container freight applies.
    # If Cape detour applies, add Cape bunker + demurrage surcharge (~$1,200/FEU)
    if "Ocean" in supplier["transport_mode"]:
        effective_freight = container_rate
        if supplier["cape_detour_applicable"] and macro_shock["cape_detour_days"] > 0:
            effective_freight += 1200.0  # Cape detour bunker surcharge
        freight_per_unit = effective_freight / cans_per_feu
    else:
        # Domestic freight / short haul (~$0.008/unit)
        freight_per_unit = 0.0085
        
    total_landed_unit_cost = metal_cost_per_unit + conversion_cost + tariff_cost + freight_per_unit
    
    # Effective lead time
    lead_time = supplier["baseline_lead_time_days"]
    if supplier["cape_detour_applicable"]:
        lead_time += macro_shock["cape_detour_days"]
        
    return {
        "total_unit_cost": total_landed_unit_cost,
        "metal_component": metal_cost_per_unit,
        "conversion_component": conversion_cost,
        "tariff_component": tariff_cost,
        "freight_component": freight_per_unit,
        "effective_lead_time": lead_time
    }

def solve_basketshield_allocation(
    suppliers_df,
    macro_shock,
    demand_units=100000,
    target_recycled_pct=0.65,
    max_avg_lead_time_days=18.0
):
    """
    Mixed-Integer Linear Programming Solver via Google OR-Tools (SCIP).
    Strict Demand Conservation + Big-M MOQ + Capacity + Recycled Targets.
    """
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return {"status": "FAILED", "message": "SCIP solver unavailable."}

    num_suppliers = len(suppliers_df)
    
    # Decision Variables:
    # x[s]: continuous volume allocated to supplier s
    # y[s]: binary indicator (1 if supplier activated, 0 otherwise)
    x = {}
    y = {}
    cost_breakdowns = []
    
    for i, (_, row) in enumerate(suppliers_df.iterrows()):
        cb = compute_supplier_landed_cost(row, macro_shock)
        cost_breakdowns.append(cb)
        
        # x_s >= 0
        x[i] = solver.NumVar(0.0, float(row["capacity_units"]), f"vol_{i}")
        # y_s in {0, 1}
        y[i] = solver.BoolVar(f"active_{i}")

    # 1. Strict Demand Conservation: sum(x_s) == demand_units
    demand_constraint = solver.Add(solver.Sum([x[i] for i in range(num_suppliers)]) == demand_units)

    # 2. Big-M Semi-Continuous MOQ Constraints:
    # x_s >= MOQ_s * y_s
    # x_s <= Capacity_s * y_s
    for i, (_, row) in enumerate(suppliers_df.iterrows()):
        moq = float(row["moq_units"])
        cap = float(row["capacity_units"])
        solver.Add(x[i] >= moq * y[i])
        solver.Add(x[i] <= cap * y[i])

    # 3. Fleet Recycled-Content Target:
    # sum(Recycled_s * x_s) >= target_recycled_pct * demand_units
    recycled_expr = solver.Sum([
        float(suppliers_df.iloc[i]["certified_recycled_content"]) * x[i] 
        for i in range(num_suppliers)
    ])
    solver.Add(recycled_expr >= target_recycled_pct * demand_units)

    # 4. Lead-Time SLA Risk Ceiling:
    # sum(LeadTime_s * x_s) <= max_avg_lead_time_days * demand_units
    lead_time_expr = solver.Sum([
        cost_breakdowns[i]["effective_lead_time"] * x[i]
        for i in range(num_suppliers)
    ])
    solver.Add(lead_time_expr <= max_avg_lead_time_days * demand_units)

    # Objective: Minimize Total Procurement Cost (Landed cost + Activation Fees)
    objective = solver.Objective()
    for i, (_, row) in enumerate(suppliers_df.iterrows()):
        c_unit = cost_breakdowns[i]["total_unit_cost"]
        act_fee = float(row["contract_activation_fee_usd"])
        objective.SetCoefficient(x[i], c_unit)
        objective.SetCoefficient(y[i], act_fee)
    objective.SetMinimization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        allocations = []
        total_procurement_cost = solver.Objective().Value()
        total_metal_cost = 0.0
        total_freight_cost = 0.0
        total_conversion_cost = 0.0
        total_tariff_cost = 0.0
        weighted_lead_time = 0.0
        weighted_recycled = 0.0

        for i, (_, row) in enumerate(suppliers_df.iterrows()):
            vol = x[i].solution_value()
            is_active = y[i].solution_value() > 0.5
            if vol > 0:
                cb = cost_breakdowns[i]
                allocations.append({
                    "supplier_id": row["id"],
                    "supplier_name": row["name"],
                    "volume_units": vol,
                    "volume_share_pct": (vol / demand_units) * 100.0,
                    "unit_cost_usd": cb["total_unit_cost"],
                    "effective_lead_time_days": cb["effective_lead_time"],
                    "certified_recycled_pct": row["certified_recycled_content"] * 100.0,
                    "is_active": is_active
                })
                total_metal_cost += cb["metal_component"] * vol
                total_conversion_cost += cb["conversion_component"] * vol
                total_tariff_cost += cb["tariff_component"] * vol
                total_freight_cost += cb["freight_component"] * vol
                weighted_lead_time += cb["effective_lead_time"] * vol
                weighted_recycled += row["certified_recycled_content"] * vol

        avg_unit_cost = total_procurement_cost / demand_units
        avg_lead_time = weighted_lead_time / demand_units
        avg_recycled = (weighted_recycled / demand_units) * 100.0

        return {
            "status": "OPTIMAL",
            "total_cost_usd": total_procurement_cost,
            "average_unit_packaging_cost": avg_unit_cost,
            "average_lead_time_days": avg_lead_time,
            "average_recycled_content_pct": avg_recycled,
            "breakdown": {
                "metal_total_usd": total_metal_cost,
                "conversion_total_usd": total_conversion_cost,
                "tariff_total_usd": total_tariff_cost,
                "freight_total_usd": total_freight_cost
            },
            "allocations": allocations
        }
    else:
        return {
            "status": "INFEASIBLE",
            "message": "No feasible allocation satisfies current MOQ, capacity, lead-time, and recycling constraints."
        }
