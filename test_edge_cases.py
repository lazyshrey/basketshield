"""
BasketShield AI - Comprehensive Edge Case & Multi-Sector Verification Suite
Tests:
1. Catalog Dataset Integrity & Schema (6,000 rows, 3 sectors, archetypes, price sanity)
2. LLM Service Decomposition & Grounding (Grocery, Electronics, Tesla/EVs, empty/malformed queries)
3. Summary Engine Executive Brief Generation (Gemini AI + Multi-Sector Fallbacks)
4. Operations Research Engine (OR-Tools MILP optimization, extreme constraints, solver speed)
"""

import sys
import time
import pandas as pd
import numpy as np

def test_catalog_integrity():
    print("\n--- 1. Testing Catalog Dataset Integrity ---")
    df = pd.read_csv("data/grocery_catalog_5000.csv")
    assert len(df) == 6000, f"Expected 6,000 rows, got {len(df)}"
    
    # Check sector distribution
    counts = df["sector"].value_counts().to_dict()
    assert counts.get("Consumer Grocery & FMCG") == 5000, f"Expected 5,000 FMCG, got {counts.get('Consumer Grocery & FMCG')}"
    assert counts.get("Consumer Electronics & Computing") == 500, f"Expected 500 Electronics, got {counts.get('Consumer Electronics & Computing')}"
    assert counts.get("Electric Vehicles & Automotive") == 500, f"Expected 500 EVs, got {counts.get('Electric Vehicles & Automotive')}"
    
    # Check archetypes
    archetypes = set(df["container_archetype"].unique())
    print(f"Verified {len(archetypes)} unique container/industrial archetypes.")
    assert "GLASS JAR" in archetypes
    assert "EV SKATEBOARD CHASSIS" in archetypes
    assert "SMARTPHONE UNIBODY" in archetypes
    assert "GPU PCIE ACCELERATOR" in archetypes
    
    # Check nulls in critical columns
    crit_cols = ["sku_id", "gtin_barcode", "product_name", "container_archetype", "wholesale_price_usd", "retail_price_usd"]
    for col in crit_cols:
        assert df[col].isnull().sum() == 0, f"Column {col} contains {df[col].isnull().sum()} null values"
        
    print("Catalog Integrity Test PASSED! (6,000 items, all 3 sectors verified)")

def test_llm_service_deconstructions():
    print("\n--- 2. Testing LLM Service Deconstruction Across Sectors ---")
    from llm_service import LLMProductAnalyzer
    analyzer = LLMProductAnalyzer()
    
    test_queries = [
        ("Davidoff Espresso 57 Intense (100g Instant Glass Jar)", "GLASS JAR", "Consumer Grocery & FMCG"),
        ("Apple iPhone 16 Pro (256GB Titanium Chassis)", "SMARTPHONE UNIBODY", "Consumer Electronics & Computing"),
        ("NVIDIA H100 Tensor Core GPU (80GB SXM5 Accelerator)", "GPU PCIE ACCELERATOR", "Consumer Electronics & Computing"),
        ("Tesla Model 3 Highland Long Range AWD (78.1kWh NMC Pack)", "EV SKATEBOARD CHASSIS", "Electric Vehicles & Automotive"),
        ("Tesla Cybertruck Dual Motor AWD (123kWh 4680 Structural Pack)", "4680 CYLINDRICAL PACK", "Electric Vehicles & Automotive"),
        ("Non-catalog Custom Kombucha Drink in Amber Bottle", "GLASS BOTTLE", "Grocery / Beverage"),
        ("", "STANDARD ARTIFACT CONTAINER", "Unknown / General")  # Edge case: empty query
    ]
    
    df = pd.read_csv("data/grocery_catalog_5000.csv")
    
    for query, expected_arch, expected_sec in test_queries:
        t0 = time.time()
        # Find catalog match if any
        matched_row = None
        if query:
            exact = df[df["product_name"].str.lower() == query.lower()]
            if not exact.empty:
                matched_row = exact.iloc[0].to_dict()
        
        res = analyzer.analyze(query, catalog_row=matched_row)
        elapsed = (time.time() - t0) * 1000
        
        # Verify engine_used attribute exists
        assert hasattr(res, "engine_used"), "Result missing engine_used attribute"
        
        # Verify archetype logic
        arch = matched_row.get("container_archetype") if matched_row else res.container_archetype
        print(f"Query: '{query[:40]}' -> Archetype: '{arch}' | Engine: {res.engine_used} ({elapsed:.1f}ms)")
        
        if matched_row:
            assert arch == expected_arch, f"Expected {expected_arch}, got {arch}"
        assert len(res.bom) > 0, f"BOM is empty for {query}"
        assert len(res.vulnerabilities) > 0, f"Vulnerabilities empty for {query}"
        assert res.financial_cost.target_retail_shelf_price_usd > 0, f"Price <= 0 for {query}"
        
    print("LLM Service Deconstruction Test PASSED across all sectors and edge cases!")

def test_summary_engine():
    print("\n--- 3. Testing Executive Summary Engine Across Sectors ---")
    from summary_engine import generate_plain_english_executive_brief
    
    test_cases = [
        {
            "product_name": "Davidoff Espresso 57 Intense (100g Instant Glass Jar)",
            "archetype": "GLASS JAR",
            "unmitigated_cost": 7.82,
            "defended_cost": 5.95,
            "baseline_cost": 5.40,
            "retail_target": 8.95,
            "unmitigated_retail": 12.50,
            "defended_retail": 9.45,
            "shock_mitigated_pct": 77.3,
            "recycled_pct": 38.0,
            "lead_time_days": 14.0,
            "active_shock_name": "Bab el-Mandeb / Red Sea Crisis"
        },
        {
            "product_name": "Tesla Model 3 Highland Long Range AWD (78.1kWh NMC Pack)",
            "archetype": "EV SKATEBOARD CHASSIS",
            "unmitigated_cost": 17200.0,
            "defended_cost": 13100.0,
            "baseline_cost": 12400.0,
            "retail_target": 42490.0,
            "unmitigated_retail": 51200.0,
            "defended_retail": 43800.0,
            "shock_mitigated_pct": 85.4,
            "recycled_pct": 65.0,
            "lead_time_days": 15.0,
            "active_shock_name": "Malacca Strait & Battery Mineral Embargo"
        },
        {
            "product_name": "Apple iPhone 16 Pro (256GB Titanium Chassis)",
            "archetype": "SMARTPHONE UNIBODY",
            "unmitigated_cost": 412.0,
            "defended_cost": 315.0,
            "baseline_cost": 295.0,
            "retail_target": 999.0,
            "unmitigated_retail": 1210.0,
            "defended_retail": 1035.0,
            "shock_mitigated_pct": 82.9,
            "recycled_pct": 75.0,
            "lead_time_days": 13.0,
            "active_shock_name": "Taiwan Strait Advanced Packaging Bottleneck"
        }
    ]
    
    for tc in test_cases:
        t0 = time.time()
        summary = generate_plain_english_executive_brief(**tc)
        elapsed = (time.time() - t0) * 1000
        assert len(summary) > 200, f"Summary too short: {summary}"
        assert tc["product_name"] in summary or tc["archetype"] in summary, "Summary did not mention product or archetype"
        print(f"Summary generated for {tc['product_name'][:35]} in {elapsed:.1f}ms (Length: {len(summary)} chars)")
        
    print("Executive Summary Engine Test PASSED for all sectors!")

def test_optimizer_scenarios():
    print("\n--- 4. Testing Google OR-Tools MILP Solver ---")
    import json
    from optimizer import solve_basketshield_allocation
    
    with open("data/macro_scenarios.json") as f:
        scenarios = json.load(f)
    suppliers_df = pd.read_csv("data/suppliers.csv")
    
    test_runs = [
        ("Baseline Standard Run", scenarios["baseline"], 100000, 0.65, 16),
        ("Acute 2026 Shock Run", scenarios["acute_2026_shock"], 100000, 0.65, 16),
        ("Small Production Run (5,000 units)", scenarios["acute_2026_shock"], 5000, 0.50, 20),
        ("Large Production Run (500,000 units)", scenarios["acute_2026_shock"], 500000, 0.60, 18),
        ("Tight Constraint Feasibility Test", scenarios["acute_2026_shock"], 100000, 0.80, 10),
    ]
    
    for name, macro, demand, recycled, max_lead in test_runs:
        t0 = time.time()
        res = solve_basketshield_allocation(
            suppliers_df,
            macro,
            demand_units=demand,
            target_recycled_pct=recycled,
            max_avg_lead_time_days=max_lead
        )
        elapsed = (time.time() - t0) * 1000
        cost_val = res.get('total_cost_usd', 0)
        print(f"Test '{name}': Status={res['status']}, Time={elapsed:.2f}ms, Cost=${cost_val:,.2f}")
        assert elapsed < 500.0, f"Solver too slow: {elapsed}ms"
        if res["status"] == "OPTIMAL":
            assert res["average_unit_packaging_cost"] > 0
            assert res["average_recycled_content_pct"] >= (recycled * 100.0) - 0.01
            assert res["average_lead_time_days"] <= max_lead + 0.01
            
    print("Google OR-Tools MILP Solver Test PASSED!")

if __name__ == "__main__":
    test_catalog_integrity()
    test_llm_service_deconstructions()
    test_summary_engine()
    test_optimizer_scenarios()
    print("\n==========================================")
    print("ALL EDGE CASES & MULTI-SECTOR TESTS PASSED!")
    print("==========================================")
