"""
BasketShield AI - Grounded Data Generator (Seed: 42)
Generates verified Bill-of-Materials (BOM), supplier contracts, and macroeconomic shock parameters
reflecting the 2026 Middle East / Hormuz / Gulf Smelter disruption and Cape detours.
"""

import os
import json
import numpy as np
import pandas as pd

def generate_grounded_dataset():
    np.random.seed(42)
    os.makedirs("data", exist_ok=True)

    # 1. Macroeconomic Shock Scenarios
    # Baseline vs 2026 Middle East Escalation (Gulf Smelter outage + Hormuz threat + Cape reroute)
    macro_scenarios = {
        "baseline": {
            "name": "Pre-Crisis Equilibrium",
            "lme_aluminum_usd_per_tonne": 2400.0,
            "us_midwest_premium_usd_per_tonne": 420.0,
            "section_232_tariff_pct": 0.0,
            "ocean_container_feu_usd": 2050.0,
            "cape_detour_days": 0,
            "gulf_smelter_capacity_loss_pct": 0.0,
            "description": "Standard trade flows via Suez Canal. Full Gulf primary smelting operational."
        },
        "moderate_shock": {
            "name": "Hormuz Transit Alert & Cape Diversion",
            "lme_aluminum_usd_per_tonne": 2950.0,
            "us_midwest_premium_usd_per_tonne": 650.0,
            "section_232_tariff_pct": 10.0,
            "ocean_container_feu_usd": 3800.0,
            "cape_detour_days": 10,
            "gulf_smelter_capacity_loss_pct": 3.0,
            "description": "Commercial shipping begins diverting around Africa; maritime insurance surcharges rise."
        },
        "acute_2026_shock": {
            "name": "2026 Acute Middle East Chokepoint Crisis",
            "lme_aluminum_usd_per_tonne": 3600.0,
            "us_midwest_premium_usd_per_tonne": 1150.0,
            "section_232_tariff_pct": 25.0,
            "ocean_container_feu_usd": 5900.0,
            "cape_detour_days": 14,
            "gulf_smelter_capacity_loss_pct": 8.0,
            "description": "Gulf primary smelters hit; Strait of Hormuz blocked; full Cape detour on Asian/Middle East packaging."
        }
    }

    with open("data/macro_scenarios.json", "w") as f:
        json.dump(macro_scenarios, f, indent=2)

    # 2. Product Bill of Materials (BOM)
    # Grounded physical specs (e.g. 13.0g 330ml beverage can, Diet Coke formulation)
    products = {
        "DIET_COKE_330ML": {
            "name": "Diet Sparkling Soda (330ml Can)",
            "retail_target_price": 1.50,
            "benchmark_wholesale_price": 0.85,
            "batch_size_units": 100000,  # 100k cans production run
            "bom_components": {
                "can_body_3104": {
                    "material": "AA 3104 Aluminum Alloy Sheet",
                    "mass_grams": 11.5,
                    "target_spec": "Drawn & Ironed Body Stock",
                    "min_recycled_content": 0.60,
                    "max_recycled_content": 0.90
                },
                "can_end_tab_5182": {
                    "material": "AA 5182 Aluminum Alloy Coil",
                    "mass_grams": 1.5,
                    "target_spec": "High-Magnesium Stay-on-Tab End",
                    "min_recycled_content": 0.30,
                    "max_recycled_content": 0.60
                },
                "liquid_concentrate": {
                    "material": "Carbonated Water + Aspartame/Acidulant Blend",
                    "mass_grams": 330.0,
                    "base_cost_per_unit": 0.085
                },
                "co2_carbonation": {
                    "material": "Food-grade CO2",
                    "base_cost_per_unit": 0.012
                }
            }
        },
        "COLD_BREW_COFFEE_250ML": {
            "name": "Single-Origin Nitro Cold Brew (250ml Can)",
            "retail_target_price": 2.95,
            "benchmark_wholesale_price": 1.65,
            "batch_size_units": 50000,
            "bom_components": {
                "can_body_3104": {
                    "material": "AA 3104 Slim Can Body",
                    "mass_grams": 10.2,
                    "target_spec": "Slim 250ml D&I Body Stock",
                    "min_recycled_content": 0.60,
                    "max_recycled_content": 0.90
                },
                "can_end_tab_5182": {
                    "material": "AA 5182 End/Tab",
                    "mass_grams": 1.3,
                    "target_spec": "200 Dia End",
                    "min_recycled_content": 0.30,
                    "max_recycled_content": 0.60
                },
                "liquid_concentrate": {
                    "material": "Cold Brewed Arabica Extract",
                    "mass_grams": 250.0,
                    "base_cost_per_unit": 0.320
                },
                "nitrogen_charge": {
                    "material": "Nitrogen Dosing",
                    "base_cost_per_unit": 0.025
                }
            }
        }
    }

    with open("data/products.json", "w") as f:
        json.dump(products, f, indent=2)

    # 3. Candidate Packaging Suppliers & Converters
    # Modeled across distinct supply routes and recycling certifications
    suppliers = [
        {
            "id": "SUP_GULF_OVERSEAS",
            "name": "Al-Bahrani Global Packaging (Gulf Smelter Dependent)",
            "location": "Bahrain / UAE",
            "base_conversion_cost_usd": 0.052,  # Low labor/energy base
            "primary_metal_exposure": 0.85,    # 85% virgin smelter ingot dependent
            "certified_recycled_content": 0.25,
            "transport_mode": "Ocean (Hormuz/Suez or Cape Detour)",
            "baseline_lead_time_days": 16,
            "cape_detour_applicable": True,
            "capacity_units": 150000,
            "moq_units": 35000,
            "contract_activation_fee_usd": 1200.0,
            "section_232_tariff_applies": True
        },
        {
            "id": "SUP_DOMESTIC_CIRCULAR",
            "name": "Aegis Circular Can-Makers (Novelis High-Recycled Sheet)",
            "location": "Domestic / Nearshore (Regional Mill)",
            "base_conversion_cost_usd": 0.068,  # Higher domestic conversion
            "primary_metal_exposure": 0.15,    # Mostly scrap/PCR closed loop
            "certified_recycled_content": 0.82, # High certified recycled content
            "transport_mode": "Domestic Rail / Freight",
            "baseline_lead_time_days": 7,
            "cape_detour_applicable": False,
            "capacity_units": 85000,
            "moq_units": 20000,
            "contract_activation_fee_usd": 800.0,
            "section_232_tariff_applies": False
        },
        {
            "id": "SUP_EURO_HYBRID",
            "name": "Danube Metal Containers (European Rolling Mill)",
            "location": "Central Europe",
            "base_conversion_cost_usd": 0.062,
            "primary_metal_exposure": 0.45,
            "certified_recycled_content": 0.65,
            "transport_mode": "Short-sea / Intermodal",
            "baseline_lead_time_days": 12,
            "cape_detour_applicable": False,
            "capacity_units": 60000,
            "moq_units": 15000,
            "contract_activation_fee_usd": 650.0,
            "section_232_tariff_applies": False
        },
        {
            "id": "SUP_EMERGENCY_BUFFER",
            "name": "Apex Quick-Response Packaging Stockist",
            "location": "Local Distribution Hub",
            "base_conversion_cost_usd": 0.085,  # Premium spot price
            "primary_metal_exposure": 0.30,
            "certified_recycled_content": 0.70,
            "transport_mode": "Dedicated Truckload",
            "baseline_lead_time_days": 3,
            "cape_detour_applicable": False,
            "capacity_units": 30000,
            "moq_units": 5000,
            "contract_activation_fee_usd": 300.0,
            "section_232_tariff_applies": False
        }
    ]

    df_suppliers = pd.DataFrame(suppliers)
    df_suppliers.to_csv("data/suppliers.csv", index=False)
    print("Grounded dataset successfully generated in data/ folder (seed 42).")

if __name__ == "__main__":
    generate_grounded_dataset()
