# Empirical Assumptions & Grounding Log (BasketShield AI)

This document formalizes all physical parameters, macroeconomic values, and contractual rules utilized by BasketShield AI.

## 1. Physical Can Metallurgy & Packaging Constants
- **Finished 330ml Can Mass:** 13.0 grams total.
  - Body: 11.5g AA 3104 alloy (manganese-rich, drawn-and-ironed).
  - Lid / Tab: 1.5g AA 5182 alloy (magnesium-rich, high tensile strength).
  - *Source:* European Patent Office (EP2941491B1); Ball Corporation Lightweighting Specifications.
- **Container Packing Density:** 130,000 empty 330ml cans per 40ft High Cube Container (FEU).
  - 20 pallets $\times$ 6,480 cans per pallet $\approx$ 129,600 cans $\approx$ 130,000 units.
  - *Source:* NOMOQ Beverage Packaging Logistics Standards (2024).

## 2. Macroeconomic Transmission Channels (2026 Crisis)
- **Primary Smelter Risk:** Middle East smelters (e.g. Alba in Bahrain, EGA in UAE) represent ~8% of global primary aluminum smelting.
- **Strait of Hormuz Blockade / Smelter Strikes:** Drives LME cash prices from \$2,400 to \$3,600/tonne and spikes US Midwest / European physical delivery premiums from \$420 to \$1,150/tonne.
  - *Source:* ING Think: "Middle East conflict tilts aluminium risks further to the upside" (2026).
- **Tariff Transmission:** Section 232 tariffs (10% to 25%) apply to imported unhedged primary metal ingots.
- **Ocean Freight Transmission:** 
  - Drewry WCI container spot rates surge from \$2,050 to \$5,900/FEU.
  - Cape of Good Hope detours add 10 to 14 days and \$1,200/FEU in emergency bunker surcharges.
  - *Transmission Arithmetic:* $+\$3,850 + \$1,200 = +\$5,050 / 130,000 \text{ cans} \approx +\$0.0388/\text{can}$.
  - *Source:* UNCTAD Review of Maritime Transport (2024).

## 3. Operations Research & Optimization Rules
- **Solver Engine:** Google OR-Tools (SCIP Backend).
- **Demand Conservation:** $\sum_{s} x_s = D_{\text{total}}$ enforced with zero slack to prevent trivial $x=0$ outcomes.
- **Semi-Continuous MOQ:** Big-$M$ binary gating where $x_s \ge \text{MOQ}_s \cdot y_s$ and $x_s \le \text{Capacity}_s \cdot y_s$ with $y_s \in \{0, 1\}$.
- **Certified Recycled Cap:** Can body sheet reaches $\ge 90\%$ recycled content; finished cans capped at 80% due to lid metallurgy constraints.
  - *Source:* Novelis Certified High-Recycled Content Program.
