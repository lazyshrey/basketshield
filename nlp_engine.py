"""
BasketShield AI - Natural Language Processing & BOM Decomposition Engine
Accepts natural language product queries (e.g. "Diet Coke 330ml can", "Olive Oil 500ml glass bottle",
"Nitro Cold Brew in tall aluminium slim can", "Red Bull energy drink") and decomposes them into
precise multi-tier physical Bills of Materials (BOM) with weights, materials, and cost baselines.
"""

import re
import json

# Pre-calibrated physical materials knowledge base
PACKAGING_ARCHETYPES = {
    "aluminum_can": {
        "material_body": "AA 3104 Aluminum Alloy Sheet (D&I)",
        "material_end": "AA 5182 Aluminum High-Magnesium Tab",
        "default_body_grams": 11.5,
        "default_end_grams": 1.5,
        "default_liquid_grams": 330.0,
        "pack_density_per_feu": 130000,
        "baseline_packaging_cost": 0.125
    },
    "slim_can": {
        "material_body": "AA 3104 Slim Alloy Sheet",
        "material_end": "AA 5182 200-Dia Stay-on-Tab End",
        "default_body_grams": 10.2,
        "default_end_grams": 1.3,
        "default_liquid_grams": 250.0,
        "pack_density_per_feu": 155000,
        "baseline_packaging_cost": 0.118
    },
    "glass_bottle": {
        "material_body": "Type-III Soda-Lime Flint Glass",
        "material_end": "Crown Cork / Tinplate Steel Cap",
        "default_body_grams": 210.0,
        "default_end_grams": 2.2,
        "default_liquid_grams": 500.0,
        "pack_density_per_feu": 42000,
        "baseline_packaging_cost": 0.220
    },
    "pet_bottle": {
        "material_body": "Virgin / rPET Polyethylene Terephthalate",
        "material_end": "HDPE Screw Closure (High-Density Polyethylene)",
        "default_body_grams": 24.5,
        "default_end_grams": 2.8,
        "default_liquid_grams": 500.0,
        "pack_density_per_feu": 75000,
        "baseline_packaging_cost": 0.095
    }
}

COMMODITY_CATEGORIES = {
    "soda": {
        "keywords": ["coke", "cola", "pepsi", "soda", "sprite", "fanta", "fizzy", "carbonated"],
        "archetype": "aluminum_can",
        "default_liquid_cost": 0.085,
        "suggested_retail": 1.50,
        "wholesale_price": 0.85,
        "ingredients": ["Filtered Carbonated Water", "Flavor Concentrate", "Non-Nutritive Sweetener (Aspartame/Acesulfame K)", "Phosphoric Acid"]
    },
    "energy": {
        "keywords": ["energy", "red bull", "monster", "caffeine", "stimulant", "taurine"],
        "archetype": "slim_can",
        "default_liquid_cost": 0.180,
        "suggested_retail": 2.75,
        "wholesale_price": 1.45,
        "ingredients": ["Carbonated Water", "Taurine & Glucuronolactone", "Caffeine Extract", "B-Group Vitamins", "Citric Acid"]
    },
    "coffee": {
        "keywords": ["coffee", "cold brew", "latte", "espresso", "arabica", "robusta", "nitro"],
        "archetype": "slim_can",
        "default_liquid_cost": 0.320,
        "suggested_retail": 2.95,
        "wholesale_price": 1.65,
        "ingredients": ["Single-Origin Steeped Coffee Extract", "Filtered Water", "Nitrogen Headspace Charge"]
    },
    "oil": {
        "keywords": ["oil", "olive", "sunflower", "canola", "vegetable oil", "cooking"],
        "archetype": "glass_bottle",
        "default_liquid_cost": 1.85,
        "suggested_retail": 6.50,
        "wholesale_price": 4.10,
        "ingredients": ["Cold-Pressed Virgin Oil", "Natural Antioxidants (Tocopherols)"]
    },
    "water": {
        "keywords": ["water", "sparkling water", "mineral", "hydration", "seltzer"],
        "archetype": "aluminum_can",
        "default_liquid_cost": 0.035,
        "suggested_retail": 1.25,
        "wholesale_price": 0.65,
        "ingredients": ["Natural Spring / Mineral Water", "Electrolyte Trace Minerals"]
    }
}

def parse_natural_product_query(query_text: str):
    """
    NLP Intent & Entity Extraction parser for consumer products.
    Extracts brand, volume size (ml/oz), packaging type, and generates grounded BOM.
    """
    clean_text = query_text.lower().strip()
    
    # 1. Volume extraction (e.g. "330ml", "250 ml", "500ml", "12 oz", "16oz")
    vol_match = re.search(r"(\d+(\.\d+)?)\s*(ml|l|oz|cl)", clean_text)
    extracted_volume_ml = 330.0  # default
    if vol_match:
        val = float(vol_match.group(1))
        unit = vol_match.group(3)
        if unit == "ml":
            extracted_volume_ml = val
        elif unit == "l":
            extracted_volume_ml = val * 1000.0
        elif unit == "cl":
            extracted_volume_ml = val * 10.0
        elif unit == "oz":
            extracted_volume_ml = val * 29.5735
            
    # 2. Packaging Archetype Detection
    archetype_key = "aluminum_can"
    if "slim" in clean_text or "250" in clean_text:
        archetype_key = "slim_can"
    elif "glass" in clean_text or "bottle" in clean_text and "pet" not in clean_text and "plastic" not in clean_text:
        archetype_key = "glass_bottle"
    elif "pet" in clean_text or "plastic" in clean_text:
        archetype_key = "pet_bottle"
        
    # 3. Category Detection
    category_key = "soda"
    for cat, meta in COMMODITY_CATEGORIES.items():
        if any(kw in clean_text for kw in meta["keywords"]):
            category_key = cat
            if "glass" not in clean_text and "pet" not in clean_text and "bottle" not in clean_text:
                archetype_key = meta["archetype"]
            break
            
    cat_meta = COMMODITY_CATEGORIES[category_key]
    arch_meta = PACKAGING_ARCHETYPES[archetype_key]
    
    # 4. Synthesize Physical Bill-of-Materials (BOM)
    # Scale body metal/glass proportionally with liquid volume if non-standard
    scale_factor = extracted_volume_ml / arch_meta["default_liquid_grams"]
    body_mass = arch_meta["default_body_grams"] * (scale_factor ** 0.67) # surface area scaling
    end_mass = arch_meta["default_end_grams"]
    
    bom = {
        "product_title": query_text.strip().title(),
        "detected_category": category_key.upper(),
        "detected_archetype": archetype_key.replace("_", " ").upper(),
        "liquid_volume_ml": extracted_volume_ml,
        "retail_target_price": cat_meta["suggested_retail"],
        "wholesale_benchmark_price": cat_meta["wholesale_price"],
        "liquid_content_cost": cat_meta["default_liquid_cost"] * scale_factor,
        "ingredients": cat_meta["ingredients"],
        "packaging_specs": {
            "body_material": arch_meta["material_body"],
            "body_mass_grams": round(body_mass, 2),
            "end_material": arch_meta["material_end"],
            "end_mass_grams": round(end_mass, 2),
            "total_packaging_mass_grams": round(body_mass + end_mass, 2),
            "pack_density_per_feu": arch_meta["pack_density_per_feu"],
            "baseline_packaging_cost": arch_meta["baseline_packaging_cost"]
        }
    }
    
    return bom

if __name__ == "__main__":
    test_queries = [
        "Diet Coke 330ml can",
        "Red Bull 250ml slim energy can",
        "Organic Extra Virgin Olive Oil 500ml glass bottle",
        "Cold Brew Nitro Coffee 250ml can"
    ]
    for q in test_queries:
        res = parse_natural_product_query(q)
        print(f"Query: '{q}' -> {res['product_title']} | Body: {res['packaging_specs']['body_mass_grams']}g | Packaging: {res['detected_archetype']}")
