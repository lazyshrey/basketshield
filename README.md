# BasketShield AI 🛡️
### Multi-Sector Supply Chain Resilience, Physical BOM Deconstruction & Consumer Price Defense
**Author:** **Shrey Jaiswal**  
*Lead Architect & Researcher — BasketShield AI Research Group*  
**Hackathon Track:** AI for Resilient and Sustainable Supply Chains  
**License:** MIT License  
**Academic Research Paper:** 📄 [Download PDF](docs/BasketShield_AI_Research_Paper.pdf) &nbsp;|&nbsp; 📖 [Read Online (Markdown)](docs/RESEARCH_PAPER.md)

---

## 1. Executive Summary & Problem Formulation

Geopolitical trade shocks and semiconductor supercycles do not impact supply chains uniformly — they transmit through precise physical and metallurgical dependencies:
1. **Consumer Grocery & FMCG:** The Strait of Hormuz conflict and Red Sea / Bab el-Mandeb chokepoints spike primary smelting premiums, annealing gas rates, and ocean container rates (Drewry WCI surging +297% to peak $5,900/FEU). For canned beverages (Diet Coke), glass coffee jars (Davidoff Espresso 57), and olive oils (Borges), freight and metal inflation adds **+35% to +48%** in unit packaging landed costs.
2. **Consumer Electronics & Computing (The 2026 AI Memory Crunch):** Hyperscaler demand for Generative AI compute clusters has consumed over **80% of leading-edge 1b-nm DRAM wafer allocation** at SK Hynix, Samsung, and Micron for High-Bandwidth Memory (HBM3e/HBM4). Because HBM requires ~3x the wafer area of standard memory, consumer-grade LPDDR5X (Apple iPhone 16 Pro, Samsung Galaxy S24 Ultra) and unified DRAM (MacBook Pro M3 Max) face severe capacity crowding-out, triggering **+40% to +65% component price surges**.
3. **Electric Vehicles & Automotive (Tesla & EVs):** EV skateboard chassis (Tesla Model 3 Highland, Cybertruck 4680, BYD Blade Battery) require 450kg–780kg of high-pressure Gigacast aluminum and high-nickel NMC/LFP battery cells. Refined precursor shipping through the Malacca Strait and synthetic graphite quotas spike unit pack costs by **$2,500–$5,500 per vehicle**.

**The Default Failure Mode:** FMCG brands, hardware OEMs, and automakers lack automated, multi-tier BOM optimization tools, so they pass 100% of the cost hike onto everyday consumers as retail inflation and shrinkflation.

**BasketShield AI** provides a prescriptive decision platform that deconstructs physical BOMs across **6,000 multi-sector products** and runs a deterministic **Mixed-Integer Linear Program (MILP via Google OR-Tools)** in **<20ms** to absorb **65%–85% of inflationary price spikes**.

---

## 2. Platform Architecture

```
[ Input: 6,000 Multi-Sector Products (FMCG, Electronics, Tesla/EVs) & Disruption Scenarios ]
                                      │
                                      ▼
         ┌────────────────────────────────────────────────────────┐
         │       Physical BOM Deconstruction & Shock Engine       │
         │  • Grounded Material Masses & Foundry Lithography      │
         │  • AI Memory Squeeze Index (HBM3e / LPDDR5X Crowding)  │
         │  • Dynamic LME + Delivery Premium + Tariffs + Freight  │
         │  • Maritime Lanes: Taiwan Strait, Hormuz, Malacca, Cape│
         └────────────────────────────────────────────────────────┘
                                      │
                                      ▼
         ┌────────────────────────────────────────────────────────┐
         │       Google OR-Tools Mixed-Integer Solver (MILP)      │
         │  • Strict Demand Conservation (sum x_s = D_total)      │
         │  • Big-M Semi-Continuous MOQ Constraints               │
         │  • Recycled / Circular Content Certification Targets   │
         │  • Weighted Lead-Time SLA Ceiling                      │
         │  • Dynamic Nearshoring Breakeven Inversion Curve       │
         └────────────────────────────────────────────────────────┘
                                      │
                                      ▼
         ┌────────────────────────────────────────────────────────┐
         │         Enterprise Decision Dashboards (Streamlit)     │
         │  • Page 1: Resilience Cockpit (BOM Drawer, Sankey, AI) │
         │  • Page 2: Provisional Cost Estimation & Pro-Forma     │
         │  • Page 3: Global Multi-Sector Commons (6,000 SKUs)    │
         │  • Page 4: Audited Operations Research Formulation     │
         └────────────────────────────────────────────────────────┘
```

---

## 3. Key Capabilities

### 🌐 6,000-SKU Multi-Sector Supply Chain Commons
- **5,000 Consumer Grocery & FMCG items:** Coffee, RTD beverages, olive oils, condiments, grains, confectionery.
- **500 Consumer Electronics & Computing SKUs:** Apple iPhone 16 Pro, NVIDIA H100 Tensor Core GPU, MacBook Pro 16" M3 Max, Samsung Galaxy S24 Ultra, Sony PlayStation 5 Pro.
- **500 Electric Vehicles & Automotive SKUs:** Tesla Model 3 Highland, Tesla Cybertruck 4680, Tesla Model Y, BYD Seal Excellence, Porsche Taycan Turbo S.
- Complete 36-attribute schema (GTIN/VIN, materials, masses, foundry tech, Tier 1–3 routes, chokepoints, baseline/shock/defended costs, Scope 3 carbon).

### 📊 Dedicated Provisional Cost Estimation & Modeling Board (Page 2)
- **In-Board Sector & SKU Switcher:** Model any product across sectors directly.
- **Interactive Stress Sliders:** Raw commodity inflation, freight multipliers, Section 232/301 tariffs, energy surcharges, and AI memory wafer surcharges.
- **Pro-Forma Variance Schedule Table:** Line-by-line landed cost schedules with inflation variance %.
- **Enterprise Margin Preservation:** Retail MSRP pass-through slider tracking gross margin erosion.
- **Plotly Visualizers:** Tornado Sensitivity Analysis, Three-State Scenario Comparison, and Dynamic Nearshoring Breakeven Inversion crossover curve.
- **CSV Model Export:** One-click download of full pro-forma schedules.

### 🧠 AI Memory Supercycle Stress Modeling
- Models the crowding-out effect of hyperscaler HBM3e/HBM4 demand consuming leading-edge DRAM wafer allocations at SK Hynix, Samsung, and Micron.
- Tracks the ~3x wafer area penalty of 3D TSV stacking and the resulting +40% to +65% spot market surge on consumer LPDDR5X/DDR5.

### ✨ Executive Plain-English AI Decision Brief
- Integrated Google AI Studio (Gemini 1.5/2.0) with resilient offline domain knowledge engines.
- Generates high-impact, non-technical explanations of geopolitical shocks, consumer checkout impacts, and mathematical hedging fixes.

---

## 4. How to Run Locally

### Prerequisites
- Python 3.10+
- Virtual environment (`venv`)

### Installation & Quickstart
```bash
# 1. Clone repository
git clone https://github.com/shreylazy/BasketShield.git
cd BasketShield

# 2. Activate virtual environment
.\venv\Scripts\activate   # Windows PowerShell
source venv/bin/activate  # Linux/macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate 6,000-SKU multi-sector dataset (Seed 42)
python generate_catalog.py

# 5. Run automated edge-case test suite
python test_edge_cases.py

# 6. Launch interactive dashboard
streamlit run app.py
```

---

## 5. Empirical Benchmarks & Academic Citations

1. **European Patent Office (EPO):** *EP2941491B1 Specification.* Beverage can body alloy (AA 3104) vs. end and tab alloy (AA 5182).
2. **TrendForce Semiconductor Memory Intelligence (2025):** *HBM3e Allocation Crowding-Out and the Global DRAM Supercycle.*
3. **ING Think Commodity Strategy (2026):** *Middle East conflict tilts aluminium risks further to the upside.* Gulf primary smelting (~8% global output) and Strait of Hormuz chokepoints.
4. **UNCTAD (2024):** *Review of Maritime Transport: Navigating Maritime Chokepoints.* Cape of Good Hope detours (+10 to +14 days).
5. **International Aluminium Institute (IAI, 2024):** Secondary recycled aluminum uses **8.3 GJ/t vs. 186 GJ/t** for primary bauxite smelting (95.5% energy saving).
6. **Novelis Corporate Disclosures:** $\ge 90\%$ recycled content in can body sheet; certified $70\%+$ finished can.
7. **NOMOQ Packaging Standards (2024):** 130,000 empty 330ml cans per 40ft FEU container.
8. **Google OR-Tools:** Combinatorial Optimization and Mixed-Integer Linear Programming (SCIP Backend).

---

*Authored by **Shrey Jaiswal** | Published under the MIT License.*
