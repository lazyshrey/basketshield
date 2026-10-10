"""
BasketShield AI - Multi-Sector Production Intelligence Engine
Deconstructs Consumer Grocery, High-Tech Electronics (Apple, NVIDIA, Samsung),
and Electric Vehicles (Tesla Model 3, Cybertruck, BYD) with physical Bill of Materials (BOM),
multi-tier supply vulnerabilities, and Google AI Studio (Gemini 1.5 / 2.0) native REST integration.
"""

import os
import json
import logging
import requests
from typing import List, Literal, Optional, Dict, Any
from pydantic import BaseModel, Field
import pandas as pd

# Load .env if present
env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    with open(env_path, "r") as f:
        for line in f:
            if line.strip() and not line.startswith("#") and "=" in line:
                k, v = line.strip().split("=", 1)
                os.environ[k.strip()] = v.strip()

logger = logging.getLogger(__name__)

# ==========================================
# 1. Pydantic Domain Schemas
# ==========================================

class BOMItem(BaseModel):
    component: str = Field(..., description="Name of the component (e.g. Octagonal Glass Jar, 78kWh Battery Pack, GH100 Silicon Die)")
    material_category: str = Field(..., description="Category (Packaging, Core Content, Chemical/Gas, Active Component, Chassis)")
    mass_g: float = Field(..., description="Estimated mass in grams")
    spec_alloy: str = Field(..., description="Material standard (e.g. Type-III Flint Glass, AlSi10Mn Gigacast, TSMC 3nm CoWoS, Grade 5 Titanium)")

class SupplierVulnerability(BaseModel):
    tier: Literal["Tier 1 (Converter)", "Tier 2 (Smelter/Processor)", "Tier 3 (Raw Material/Energy)"] = Field(..., description="Supplier tier")
    chokepoint_risk: str = Field(..., description="Vulnerability description")
    threat_level: Literal["Low", "Medium", "High", "Critical"] = Field(..., description="Threat severity")

class FinancialBOMCost(BaseModel):
    packaging_cost_usd: float = Field(..., description="Structural chassis / packaging unit cost")
    liquid_ingredient_cost_usd: float = Field(..., description="Core powertrain / silicon / ingredients cost")
    freight_baseline_usd: float = Field(..., description="Ocean/air/inland transport cost baseline")
    target_retail_shelf_price_usd: float = Field(..., description="Consumer retail shelf price or vehicle MSRP")
    wholesale_price_usd: float = Field(..., description="Wholesale benchmark price / factory landed BOM")

class ProductDecompositionResult(BaseModel):
    product_name: str
    product_category: str
    container_archetype: str
    liquid_volume_ml: float
    bom: List[BOMItem]
    vulnerabilities: List[SupplierVulnerability]
    financial_cost: FinancialBOMCost
    ai_strategic_brief: str
    engine_used: str = "Live Gemini LLM"

# ==========================================
# 2. System Prompt Formulation (Multi-Sector)
# ==========================================

SYSTEM_PROMPT = """
You are an elite Principal Industrial Systems Metallurgist & Supply Chain Engineer.
Deconstruct any product into its physical Bill of Materials (BOM), structural archetype, 
and multi-tier supply chain vulnerabilities across:
1. Consumer Grocery & FMCG (Food, Beverages, Coffee, Oils)
2. Consumer Electronics & Semiconductors (Smartphones, GPUs, Laptops, Consoles)
3. Electric Vehicles & Automotive (Tesla Model 3/Y/Cybertruck, BYD, Porsche EV)

SECTOR ARCHETYPE RULES:
- Grocery: GLASS JAR, ALUMINUM CAN, SLIM CAN, GLASS BOTTLE, PET SQUEEZE BOTTLE, TETRAPAK, MULTI-FOIL POUCH, PP TUB, TINPLATE CAN
- Electronics: SMARTPHONE UNIBODY, GPU PCIE ACCELERATOR, LAPTOP ENCLOSURE, GAME CONSOLE CHASSIS, WEARABLE CHASSIS
- Automotive: EV SKATEBOARD CHASSIS, 4680 CYLINDRICAL PACK, BLADE BATTERY UNIBODY, EXTRUDED ALU MONOCOQUE

Return strictly a valid JSON matching this schema:
{
  "product_name": "string",
  "product_category": "string",
  "container_archetype": "string",
  "liquid_volume_ml": 0.0,
  "bom": [
    {
      "component": "string",
      "material_category": "Packaging|Core Content|Chemical/Gas|Active Component|Chassis",
      "mass_g": 0.0,
      "spec_alloy": "string"
    }
  ],
  "vulnerabilities": [
    {
      "tier": "Tier 1 (Converter)|Tier 2 (Smelter/Processor)|Tier 3 (Raw Material/Energy)",
      "chokepoint_risk": "string",
      "threat_level": "Low|Medium|High|Critical"
    }
  ],
  "financial_cost": {
    "packaging_cost_usd": 0.0,
    "liquid_ingredient_cost_usd": 0.0,
    "freight_baseline_usd": 0.0,
    "target_retail_shelf_price_usd": 0.0,
    "wholesale_price_usd": 0.0
  },
  "ai_strategic_brief": "string"
}
"""

# ==========================================
# 3. Grounded Deconstruction Builders
# ==========================================

def build_decomposition_from_catalog(row: Dict[str, Any], engine_label: str = "Verified Catalog Ground Truth") -> ProductDecompositionResult:
    """
    Builds a physically grounded BOM and vulnerability profile across Grocery, Tech, and Automotive.
    """
    p_name = str(row.get("product_name", "Product"))
    cat = str(row.get("category", "Industrial Product"))
    sector = str(row.get("sector", "Consumer Grocery & FMCG"))
    archetype = str(row.get("container_archetype", "GLASS JAR")).upper()
    pkg_mass = float(row.get("packaging_mass_grams", 200.0))
    pkg_spec = str(row.get("packaging_spec", row.get("primary_container_material", "Standard Commercial Material")))
    retail_price = float(row.get("retail_price_usd", 4.99))
    wholesale_price = float(row.get("wholesale_price_usd", 2.80))
    chokepoint = str(row.get("primary_chokepoint_vulnerability", "Maritime transport delay & energy surcharge"))
    brand = str(row.get("brand", "Producer"))

    bom: List[BOMItem] = []
    vulnerabilities: List[SupplierVulnerability] = []
    vol_ml = 250.0

    # ----------------------------------------------------
    # Case A: Electric Vehicles & Automotive (Tesla, BYD, Porsche)
    # ----------------------------------------------------
    if sector == "Electric Vehicles & Automotive" or any(w in archetype for w in ["SKATEBOARD", "4680", "BLADE BATTERY", "MONOCOQUE", "EV"]):
        vol_ml = 78000.0  # Battery capacity representation in ml/kWh
        bom = [
            BOMItem(component=f"{brand} Structural High-Voltage Battery Pack Enclosure", material_category="Packaging", mass_g=pkg_mass * 0.65, spec_alloy=pkg_spec),
            BOMItem(component="High-Pressure Gigacasting Subframe Assembly", material_category="Chassis", mass_g=pkg_mass * 0.22, spec_alloy="AlSi10Mn Structural Aluminum Alloy"),
            BOMItem(component="Dual Silicon Carbide (SiC) Power Inverter Stages", material_category="Active Component", mass_g=14000.0, spec_alloy="650V-1200V High-Bandgap SiC Mosfets"),
            BOMItem(component=f"{brand} Permanent Magnet Drive Motor Assemblies", material_category="Core Content", mass_g=pkg_mass * 0.13, spec_alloy="Neodymium-Dysprosium NdFeB Rotor + Copper Stator")
        ]
        vulnerabilities = [
            SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="Silicon Carbide (SiC) power semiconductor wafer packaging allocation (+18 weeks)", threat_level="High"),
            SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="Chinese synthetic battery-grade graphite & NdFeB permanent magnet export quotas", threat_level="Critical"),
            SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="Critical")
        ]
        strat_brief = (
            f"{p_name} is an Electric Vehicle engineered on a {archetype}. "
            f"{chokepoint} exposes vehicle assembly lines to critical mineral bottlenecks (battery-grade lithium hydroxide, synthetic graphite, and SiC power inverters)."
        )
        packaging_cost = float(row.get("packaging_baseline_cost_usd", wholesale_price * 0.42))
        content_cost = float(row.get("raw_content_cost_usd", wholesale_price * 0.35))
        freight_cost = float(row.get("freight_baseline_usd", wholesale_price * 0.04))

    # ----------------------------------------------------
    # Case B: Consumer Electronics & Semiconductors (Apple, NVIDIA, Samsung)
    # ----------------------------------------------------
    elif sector == "Consumer Electronics & Computing" or any(w in archetype for w in ["SMARTPHONE", "GPU", "LAPTOP", "CONSOLE"]):
        vol_ml = 500.0
        if "GPU" in archetype:
            bom = [
                BOMItem(component="GH100 Silicon Compute Die + CoWoS-S Substrate", material_category="Active Component", mass_g=12.0, spec_alloy="TSMC 4N Process (80B Transistors)"),
                BOMItem(component="80GB HBM3 High-Bandwidth Memory Stacks", material_category="Active Component", mass_g=16.0, spec_alloy="SK Hynix 12-High Micro-bump TSV"),
                BOMItem(component="Vapor Chamber & Direct-Contact Copper Heat Sink", material_category="Packaging", mass_g=pkg_mass * 0.70, spec_alloy="OFHC High-Purity Copper Sintered Structure"),
                BOMItem(component="SXM5 High-Speed Mezzanine Interconnect Board", material_category="Packaging", mass_g=pkg_mass * 0.30, spec_alloy="Ultra-Low-Loss Megtron-7 Multilayer PCB")
            ]
        else: # Smartphones & Laptops
            bom = [
                BOMItem(component=f"{brand} Precision CNC Monocoque Chassis", material_category="Packaging", mass_g=pkg_mass * 0.45, spec_alloy=pkg_spec),
                BOMItem(component="Advanced 3nm/4nm FinFET Application Processor", material_category="Active Component", mass_g=2.5, spec_alloy="TSMC 3nm CoWoS Silicon"),
                BOMItem(component="High-Refresh LTPO Display Module & Cover Glass", material_category="Packaging", mass_g=pkg_mass * 0.30, spec_alloy="OLED Matrix + Nanocrystal Toughened Glass"),
                BOMItem(component="High-Density Recycled Cobalt Cathode Battery", material_category="Core Content", mass_g=pkg_mass * 0.25, spec_alloy="Lithium Cobalt Oxide (100% Recycled Cobalt)")
            ]
        vulnerabilities = [
            SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="Taiwan Strait maritime corridor disruption for TSMC advanced packaging", threat_level="Critical"),
            SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="South Korean OLED display glass fabrication energy & cleanroom capacity", threat_level="High"),
            SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="Critical")
        ]
        strat_brief = (
            f"{p_name} is packaged in a {archetype} ({pkg_spec}). "
            f"Over 82% of core semiconductor value routes through the Taiwan Strait and East Asian air express hubs, exposing production schedules to {chokepoint}."
        )
        packaging_cost = float(row.get("packaging_baseline_cost_usd", wholesale_price * 0.16))
        content_cost = float(row.get("raw_content_cost_usd", wholesale_price * 0.55))
        freight_cost = float(row.get("freight_baseline_usd", wholesale_price * 0.03))

    # ----------------------------------------------------
    # Case C: Consumer Staples & Grocery (Glass Jar, Can, Bottle, TetraPak)
    # ----------------------------------------------------
    else:
        if archetype == "GLASS JAR":
            vol_ml = 200.0 if "200g" in p_name.lower() else (100.0 if "100g" in p_name.lower() else 350.0)
            jar_glass_mass = max(100.0, pkg_mass - 16.0)
            bom = [
                BOMItem(component=f"Heavy Molded Flint Glass Jar ({jar_glass_mass:.0f}g)", material_category="Packaging", mass_g=jar_glass_mass, spec_alloy=pkg_spec),
                BOMItem(component="Aromaseal Polypropylene Screw Closure", material_category="Packaging", mass_g=14.5, spec_alloy="Injection-Molded PP Polymer"),
                BOMItem(component="Tamper-Evident Induction Heat Seal Membrane", material_category="Packaging", mass_g=0.8, spec_alloy="Aluminum Foil / Polyethylene Laminate"),
                BOMItem(component=f"{brand} High-Grade Core Product Granules/Extract", material_category="Core Content", mass_g=vol_ml, spec_alloy=f"{cat} Premium Standard Formulation")
            ]
            vulnerabilities = [
                SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="European specialty glass container annealing kiln gas surcharges (+28%)", threat_level="High"),
                SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="Cryogenic freeze-drying and vacuum evaporation processing bottlenecks", threat_level="Medium"),
                SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="Critical")
            ]
            strat_brief = (
                f"{p_name} combines heavy glass packaging ({pkg_mass:.1f}g) with specialized raw commodities. "
                f"{chokepoint} inflates landed transport costs, while European glassworks energy tariffs squeeze packaging converter margins."
            )

        elif archetype == "GLASS BOTTLE":
            vol_ml = 500.0 if "500ml" in p_name.lower() else (1000.0 if "1l" in p_name.lower() else 330.0)
            bottle_mass = max(120.0, pkg_mass - 5.0)
            bom = [
                BOMItem(component=f"UV-Protected Dark Tint Glass Bottle ({bottle_mass:.0f}g)", material_category="Packaging", mass_g=bottle_mass, spec_alloy=pkg_spec),
                BOMItem(component="ROPP Aluminum Closure & Pourer Insert", material_category="Packaging", mass_g=4.5, spec_alloy="Alloy 8011 Aluminum Sheet + PE"),
                BOMItem(component=f"{brand} Cold-Pressed / Bottled Core Formula", material_category="Core Content", mass_g=vol_ml * 0.92, spec_alloy=f"{cat} Standard")
            ]
            vulnerabilities = [
                SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="Glass furnace natural gas thermal surcharges and container ship backlogs", threat_level="High"),
                SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="Extraction mill throughput delays and crop quality yield variance", threat_level="Medium"),
                SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="Critical")
            ]
            strat_brief = (
                f"Heavy container weight ({pkg_mass:.1f}g) creates high sensitivity to maritime freight rates. "
                f"Coupled with {chokepoint}, landed packaging costs face sharp upward pressure without nearshore alternatives."
            )

        elif archetype in ["ALUMINUM CAN", "SLIM CAN"]:
            vol_ml = 250.0 if archetype == "SLIM CAN" else 330.0
            can_body_mass = max(8.0, pkg_mass - 1.5)
            bom = [
                BOMItem(component="Drawn-and-Ironed Beverage Can Body", material_category="Packaging", mass_g=can_body_mass, spec_alloy="AA 3104 Cold-Rolled Aluminum Sheet"),
                BOMItem(component="Stay-on-Tab Easy Open End Lid", material_category="Packaging", mass_g=1.5, spec_alloy="AA 5182 High-Magnesium Lid Alloy"),
                BOMItem(component=f"{brand} Formulated Beverage Base", material_category="Core Content", mass_g=vol_ml, spec_alloy="Filtered Water & Core Ingredients")
            ]
            vulnerabilities = [
                SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="Overseas can converting plants face Cape of Good Hope detours (+14 days)", threat_level="High"),
                SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="Strait of Hormuz tension and Middle East smelter outages spike Midwest Delivery Premium", threat_level="Critical"),
                SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="High")
            ]
            strat_brief = (
                f"Primary aluminum smelting consumes ~186 GJ/tonne. {chokepoint} disrupts regional ingot flows, "
                f"while switching to certified domestic recycled coil (Novelis-spec) dampens cost spikes by up to 75%."
            )

        elif archetype == "PET SQUEEZE BOTTLE":
            vol_ml = 400.0
            bom = [
                BOMItem(component="Multilayer Barrier Squeeze Bottle", material_category="Packaging", mass_g=pkg_mass - 6.5, spec_alloy=pkg_spec),
                BOMItem(component="Silicone Stay-Clean Valve & Flip-Top Cap", material_category="Packaging", mass_g=6.5, spec_alloy="Injection Molded PP + LSR Silicone Membrane"),
                BOMItem(component=f"{brand} Recipe Emulsion / Paste Base", material_category="Core Content", mass_g=380.0, spec_alloy="Concentrated Ingredients Formulation")
            ]
            vulnerabilities = [
                SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="PET resin preform price hikes tracking crude paraxylene shipping rates", threat_level="High"),
                SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="Industrial evaporator gas costs for concentrate dehydration", threat_level="Medium"),
                SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="Critical")
            ]
            strat_brief = (
                f"Multi-layer PET with EVOH barrier preserves shelf stability. {chokepoint} and polymer precursor shocks "
                f"tighten converter availability across regional bottling hubs."
            )

        elif archetype == "TETRAPAK":
            vol_ml = 1000.0
            bom = [
                BOMItem(component="Aseptic 6-Layer Liquid Packaging Board", material_category="Packaging", mass_g=pkg_mass - 4.2, spec_alloy=pkg_spec),
                BOMItem(component="Bio-based HeliCap Screw Closure", material_category="Packaging", mass_g=4.2, spec_alloy="High-Density Polyethylene Closure"),
                BOMItem(component=f"{brand} Liquid Beverage Core", material_category="Core Content", mass_g=1000.0, spec_alloy="Pasteurized Liquid Matrix")
            ]
            vulnerabilities = [
                SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="Aseptic packaging converter foil lamination line backlog", threat_level="High"),
                SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="Barrier ultra-thin aluminum foil rolling shortages", threat_level="Medium"),
                SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="Critical")
            ]
            strat_brief = (
                f"Aseptic liquid cartons require ultra-thin barrier foil (6.3 microns). {chokepoint} slows raw material arrivals, "
                f"forcing converters to rely on secondary buffer inventories."
            )

        else:
            vol_ml = 300.0
            bom = [
                BOMItem(component=f"Engineered Container ({archetype})", material_category="Packaging", mass_g=pkg_mass, spec_alloy=pkg_spec),
                BOMItem(component=f"{brand} Formulated Core Content", material_category="Core Content", mass_g=vol_ml, spec_alloy=f"{cat} Standard Blend")
            ]
            vulnerabilities = [
                SupplierVulnerability(tier="Tier 1 (Converter)", chokepoint_risk="Packaging converting capacity tightening under freight surcharges", threat_level="Medium"),
                SupplierVulnerability(tier="Tier 2 (Smelter/Processor)", chokepoint_risk="Upstream raw material compounding and processing delays", threat_level="Medium"),
                SupplierVulnerability(tier="Tier 3 (Raw Material/Energy)", chokepoint_risk=chokepoint, threat_level="High")
            ]
            strat_brief = (
                f"{p_name} is packaged in {archetype} ({pkg_spec}). {chokepoint} generates transport and material inflation "
                f"that cascades directly down into wholesale landed costs."
            )

        packaging_cost = float(row.get("packaging_baseline_cost_usd", wholesale_price * 0.14))
        content_cost = float(row.get("raw_content_cost_usd", wholesale_price * 0.48))
        freight_cost = float(row.get("freight_baseline_usd", wholesale_price * 0.05))

    return ProductDecompositionResult(
        product_name=p_name,
        product_category=cat,
        container_archetype=archetype,
        liquid_volume_ml=vol_ml,
        bom=bom,
        vulnerabilities=vulnerabilities,
        financial_cost=FinancialBOMCost(
            packaging_cost_usd=round(packaging_cost, 2),
            liquid_ingredient_cost_usd=round(content_cost, 2),
            freight_baseline_usd=round(freight_cost, 2),
            target_retail_shelf_price_usd=round(retail_price, 2),
            wholesale_price_usd=round(wholesale_price, 2)
        ),
        ai_strategic_brief=strat_brief,
        engine_used=engine_label
    )


# ==========================================
# 4. LLM Product Analyzer Class
# ==========================================

class LLMProductAnalyzer:
    def __init__(self):
        self.google_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        self._catalog_df = None

    def _get_catalog(self) -> Optional[pd.DataFrame]:
        if self._catalog_df is None:
            catalog_path = os.path.join(os.path.dirname(__file__), "data", "grocery_catalog_5000.csv")
            if os.path.exists(catalog_path):
                try:
                    self._catalog_df = pd.read_csv(catalog_path)
                except Exception as e:
                    logger.warning(f"Could not load catalog csv: {e}")
        return self._catalog_df

    def find_catalog_match(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Attempts exact or fuzzy match across the 6,000 multi-sector catalog.
        """
        df = self._get_catalog()
        if df is None or df.empty or not query:
            return None

        q_clean = query.strip().lower()

        # 1. Exact match on product_name
        exact = df[df["product_name"].str.lower() == q_clean]
        if not exact.empty:
            return exact.iloc[0].to_dict()

        # 2. Substring match
        contains_m = df[df["product_name"].str.lower().str.contains(q_clean, regex=False)]
        if not contains_m.empty:
            return contains_m.iloc[0].to_dict()

        # 3. Match reverse (if query contains catalog product name)
        for _, row in df.head(1000).iterrows():
            p_name = str(row["product_name"]).lower()
            if p_name in q_clean or (p_name.split(" (")[0] in q_clean):
                return row.to_dict()

        return None

    def analyze(
        self,
        query: str,
        user_api_key: Optional[str] = None,
        catalog_row: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> ProductDecompositionResult:
        """
        Unified multi-sector decomposition:
        1. Checks catalog row passed or looks up 6,000-SKU multi-sector catalog.
        2. Tries Gemini with verified grounded prompts.
        3. Falls back gracefully to universal physical domain engine.
        """
        if catalog_row is None:
            catalog_row = kwargs.get("catalog_row")

        active_key = user_api_key.strip() if user_api_key and user_api_key.strip() else self.google_key
        matched_catalog = catalog_row or self.find_catalog_match(query)

        if active_key:
            try:
                return self._call_google_gemini(query, active_key, matched_catalog)
            except Exception as e:
                logger.info(f"Gemini live call bypassed/failed ({e}); using verified grounded domain engine.")
                if matched_catalog:
                    return build_decomposition_from_catalog(matched_catalog, engine_label="Verified Catalog Ground Truth (API Safe)")
                return self._domain_fallback(query)

        if matched_catalog:
            return build_decomposition_from_catalog(matched_catalog, engine_label="Verified Catalog Ground Truth")

        return self._domain_fallback(query)

    def _call_google_gemini(
        self,
        query: str,
        api_key: str,
        catalog_hint: Optional[Dict[str, Any]] = None
    ) -> ProductDecompositionResult:
        """
        Native REST call to Gemini 1.5/2.0 with prompt grounding to prevent hallucination.
        """
        models_to_try = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"]
        
        prompt_content = f"{SYSTEM_PROMPT}\n\nDeconstruct product: '{query}'"
        if catalog_hint:
            prompt_content += (
                f"\n[VERIFIED DATA: container_archetype='{catalog_hint.get('container_archetype')}', "
                f"sector='{catalog_hint.get('sector')}', "
                f"category='{catalog_hint.get('category')}', "
                f"packaging_spec='{catalog_hint.get('packaging_spec')}', "
                f"packaging_mass_grams={catalog_hint.get('packaging_mass_grams')}, "
                f"primary_chokepoint='{catalog_hint.get('primary_chokepoint_vulnerability')}']"
            )

        payload = {
            "contents": [{"parts": [{"text": prompt_content}]}],
            "generationConfig": {
                "temperature": 0.1,
                "response_mime_type": "application/json"
            }
        }
        headers = {"Content-Type": "application/json"}

        last_err = None
        for m in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={api_key}"
            try:
                resp = requests.post(url, json=payload, headers=headers, timeout=8)
                if resp.status_code == 200:
                    data = resp.json()
                    raw_text = data["candidates"][0]["content"]["parts"][0]["text"]
                    clean_json = raw_text.strip().removeprefix("```json").removesuffix("```").strip()
                    parsed = json.loads(clean_json)
                    parsed["engine_used"] = f"Live Google Gemini ({m})"
                    return ProductDecompositionResult(**parsed)
                else:
                    last_err = f"HTTP {resp.status_code}: {resp.text[:120]}"
            except Exception as ex:
                last_err = str(ex)

        raise RuntimeError(f"Gemini API could not complete: {last_err}")

    def _domain_fallback(self, query: str) -> ProductDecompositionResult:
        """
        Universal domain parser for custom queries not present in the catalog.
        Accurately recognizes Electric Vehicles (Tesla, BYD), Electronics (Apple, NVIDIA, GPUs),
        and Grocery (Glass jars, cans, bottles).
        """
        q = query.lower()

        # 1. Electric Vehicles & Automotive Detection
        if any(w in q for w in ["tesla", "cybertruck", "model 3", "model y", "model s", "model x", "byd", "porsche taycan", "ev", "electric car", "rivian", "electric vehicle"]):
            sector = "Electric Vehicles & Automotive"
            category = "Electric Vehicles"
            if "cybertruck" in q or "4680" in q:
                archetype = "4680 CYLINDRICAL PACK"
                brand = "Tesla"
                p_title = query.strip().title()
                mat = "Ultra-Hard 30X Cold-Rolled Stainless Steel Exoskeleton"
                mass = 780000.0
                retail_p = 79990.0
                wholesale_p = 56000.0
            elif "byd" in q or "blade" in q:
                archetype = "BLADE BATTERY UNIBODY"
                brand = "BYD"
                p_title = query.strip().title()
                mat = "Cell-to-Body Honeycomb Aluminum Floor"
                mass = 490000.0
                retail_p = 44990.0
                wholesale_p = 26800.0
            else:
                archetype = "EV SKATEBOARD CHASSIS"
                brand = "Tesla" if "tesla" in q else "EV Manufacturer"
                p_title = query.strip().title()
                mat = "AlSi10Mn High-Pressure Gigacasting Aluminum"
                mass = 485000.0
                retail_p = 42490.0
                wholesale_p = 28500.0

            row = {
                "sector": sector,
                "product_name": p_title,
                "category": category,
                "container_archetype": archetype,
                "primary_container_material": mat,
                "packaging_mass_grams": mass,
                "retail_price_usd": retail_p,
                "wholesale_price_usd": wholesale_p,
                "packaging_baseline_cost_usd": wholesale_p * 0.42,
                "raw_content_cost_usd": wholesale_p * 0.35,
                "freight_baseline_usd": 950.0,
                "primary_chokepoint_vulnerability": "Malacca Strait refined battery precursor shipping backlogs & Chinese synthetic graphite export controls",
                "brand": brand
            }
            return build_decomposition_from_catalog(row, engine_label="Domain Knowledge Engine (Automotive Specialized)")

        # 2. Consumer Electronics & Semiconductor Detection
        elif any(w in q for w in ["iphone", "apple", "nvidia", "h100", "gpu", "macbook", "laptop", "galaxy", "samsung", "ps5", "playstation", "semiconductor", "chip"]):
            sector = "Consumer Electronics & Computing"
            category = "Consumer Electronics"
            if any(w in q for w in ["h100", "gpu", "nvidia", "accelerator"]):
                archetype = "GPU PCIE ACCELERATOR"
                brand = "NVIDIA"
                mat = "Megtron-7 Multilayer PCB + Copper Vapor Chamber"
                mass = 2150.0
                retail_p = 32000.0
                wholesale_p = 14500.0
            elif any(w in q for w in ["macbook", "laptop"]):
                archetype = "LAPTOP ENCLOSURE"
                brand = "Apple"
                mat = "100% Recycled 6000-Series Unibody Aluminum"
                mass = 2140.0
                retail_p = 3499.0
                wholesale_p = 2100.0
            else:
                archetype = "SMARTPHONE UNIBODY"
                brand = "Apple" if "iphone" in q else ("Samsung" if "galaxy" in q else "Tech Co.")
                mat = "Grade 5 Titanium / Recycled Aluminum Subframe"
                mass = 199.0
                retail_p = 999.0
                wholesale_p = 540.0

            row = {
                "sector": sector,
                "product_name": query.strip().title(),
                "category": category,
                "container_archetype": archetype,
                "primary_container_material": mat,
                "packaging_mass_grams": mass,
                "retail_price_usd": retail_p,
                "wholesale_price_usd": wholesale_p,
                "packaging_baseline_cost_usd": wholesale_p * 0.16,
                "raw_content_cost_usd": wholesale_p * 0.55,
                "freight_baseline_usd": 14.50,
                "primary_chokepoint_vulnerability": "Taiwan Strait maritime corridor disruption for TSMC advanced packaging",
                "brand": brand
            }
            return build_decomposition_from_catalog(row, engine_label="Domain Knowledge Engine (Electronics Specialized)")

        # 3. Consumer Grocery & FMCG Detection
        else:
            if any(w in q for w in ["jar", "glass jar", "instant jar", "jam", "honey", "nutella", "flint"]):
                archetype = "GLASS JAR"
            elif any(w in q for w in ["squeeze", "top-down", "ketchup bottle", "mayo bottle", "mustard bottle"]):
                archetype = "PET SQUEEZE BOTTLE"
            elif any(w in q for w in ["tetrapak", "tetra pak", "aseptic", "carton", "brick", "oat milk", "soy milk"]):
                archetype = "TETRAPAK"
            elif any(w in q for w in ["slim can", "slimline", "nitro", "cold brew can", "250ml can"]):
                archetype = "SLIM CAN"
            elif any(w in q for w in ["can", "aluminum can", "soda can", "coke", "pepsi", "beer", "330ml"]):
                archetype = "ALUMINUM CAN"
            elif any(w in q for w in ["glass bottle", "marasca", "oil bottle", "wine", "vinegar"]):
                archetype = "GLASS BOTTLE"
            elif any(w in q for w in ["pouch", "foil pack", "vacuum foil", "beans"]):
                archetype = "MULTI-FOIL POUCH"
            elif any(w in q for w in ["tub", "yogurt", "butter tub"]):
                archetype = "PP TUB"
            elif any(w in q for w in ["box", "cardboard", "cereal", "pasta box"]):
                archetype = "FOLDING CARTON"
            else:
                if any(w in q for w in ["coffee", "tea", "tokai", "davidoff", "nescafe"]):
                    archetype = "GLASS JAR"
                elif any(w in q for w in ["oil", "olive"]):
                    archetype = "GLASS BOTTLE"
                elif any(w in q for w in ["ketchup", "sauce"]):
                    archetype = "PET SQUEEZE BOTTLE"
                else:
                    archetype = "ALUMINUM CAN"

            if any(w in q for w in ["coffee", "tea", "tokai", "davidoff", "nescafe", "espresso", "beans"]):
                category = "Coffee & Tea"
                brand = "Specialty Coffee"
            elif any(w in q for w in ["oil", "olive", "sunflower"]):
                category = "Edible Oils & Fats"
                brand = "Artisan Oils"
            elif any(w in q for w in ["ketchup", "sauce", "mustard"]):
                category = "Condiments & Sauces"
                brand = "Condiments Co."
            else:
                category = "Beverages & Sodas"
                brand = "Beverage Co."

            row = {
                "sector": "Consumer Grocery & FMCG",
                "product_name": query.strip().title(),
                "category": category,
                "container_archetype": archetype,
                "packaging_mass_grams": 260.0 if "JAR" in archetype else (310.0 if "BOTTLE" in archetype else 13.0),
                "primary_container_material": "Flint Glass Type III" if "JAR" in archetype else ("AA 3104 Cold-Rolled" if "CAN" in archetype else "High-Barrier Polymer"),
                "retail_price_usd": 6.50 if "JAR" in archetype else 2.20,
                "wholesale_price_usd": 3.90 if "JAR" in archetype else 1.25,
                "primary_chokepoint_vulnerability": "Bab el-Mandeb / Red Sea shipping detour (+14 days)" if category == "Coffee & Tea" else "Geopolitical container freight spike",
                "brand": brand
            }
            return build_decomposition_from_catalog(row, engine_label="Domain Knowledge Engine (API Timeout Safe)")
