# BasketShield AI 🛡️
### Multi-Tier FMCG Packaging & Sourcing Optimization Engine
**Event:** COMMIT FOR GOOD 2026  
**Domain:** AI for Resilient and Sustainable Supply Chains  
**License:** MIT License  

---

## 1. Problem Statement
When geopolitical conflict in the Middle East threatened the **Strait of Hormuz** and damaged Gulf primary smelters (~8% of global primary aluminum smelting), the primary transmission mechanism was not container freight alone, but a structural surge in **LME aluminum cash prices, regional physical delivery premiums (US Midwest / Rotterdam Duty-Paid), and Section 232 tariffs** (ING Think, 2026).

Container disruptions (Cape of Good Hope detours adding 10–14 days and container surcharges) compound this shock for packaging converters. With **~130,000 empty 330ml cans packed per 40ft container (FEU)** (NOMOQ, 2024), ocean freight rate spikes add **+$0.030/can**, while metal and tariff spikes add **+$0.015 to $0.025/can**. 

Unhedged consumer brands and bottlers face an unmitigated **+$0.045–$0.060 (+35% to +48%) surge in unit packaging costs**, which is traditionally passed directly onto everyday consumers at the supermarket shelf as price inflation and shrinkflation.

---

## 2. Solution Architecture
**BasketShield AI** is an open-source prescriptive decision engine built with **Python, Google OR-Tools (MILP/SCIP), Streamlit, and Plotly**.

```
[ Input: FMCG Product (Diet Coke Can) & Geopolitical Shock Scenario ]
                                │
                                ▼
         ┌──────────────────────────────────────────────┐
         │       BOM Decomposition & Freight Engine     │
         │  • 13.0g Can Mass (11.5g 3104 + 1.5g 5182)   │
         │  • Dynamic LME + Midwest Premium + Tariffs   │
         │  • Ocean Container & Cape Detour Surcharges  │
         └──────────────────────────────────────────────┘
                                │
                                ▼
         ┌──────────────────────────────────────────────┐
         │     Google OR-Tools Mixed-Integer Solver     │
         │  • Strict Demand Conservation (sum x = D)    │
         │  • Big-M Semi-Continuous MOQ Constraints     │
         │  • Recycled-Content Certification Targets    │
         │  • Lead-Time SLA Risk Ceiling                │
         └──────────────────────────────────────────────┘
                                │
                                ▼
[ Output: Defended Retail Shelf Price ($1.50) & 75% Cost Shock Mitigation ]
```

---

## 3. How to Run Locally

### Prerequisites
- Python 3.10+
- Virtual environment (`venv`)

### Installation & Run
```bash
# 1. Clone repository
git clone https://github.com/your-username/BasketShield.git
cd BasketShield

# 2. Activate virtual environment
.\venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/macOS

# 3. Install requirements
pip install -r requirements.txt

# 4. Generate grounded baseline data (seed 42)
python data_generate.py

# 5. Launch interactive dashboard
streamlit run app.py
```

---

## 4. Empirical Grounding & Verified Benchmarks
- **EP2941491B1 Specification:** Beverage can body alloy (AA 3104) vs. end and tab alloy (AA 5182).
- **International Aluminium Institute (IAI):** Recycled aluminum requires **8.3 GJ/tonne vs. 186 GJ/tonne** for primary smelting (95.5% energy saving).
- **ING Think (2026):** Gulf smelter primary capacity risk and Strait of Hormuz chokepoint premium transmission.
- **UNCTAD (2024):** Review of Maritime Transport: Cape of Good Hope detours (+10 to +14 days).
- **NOMOQ Specifications:** 130,000 empty 330ml cans per 40ft FEU container.
- **Novelis Disclosures:** $\ge 90\%$ recycled content in can body sheet; certified $70\%+$ finished can.
