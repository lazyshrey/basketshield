"""
BasketShield AI - Multi-Sector Supply Chain Research Dataset Generator (Seed 42)
Generates an extensive, highly realistic 6,000-item multi-sector supply chain dataset across:
1. Consumer Grocery & FMCG (5,000 items)
2. Consumer Electronics & Semiconductor Computing (500 items: Apple, NVIDIA, Samsung, Sony)
3. Electric Vehicles & Automotive (500 items: Tesla, BYD, Porsche, Ford, Rivian)

Complete 36-attribute schema covering:
- Commercial Identity (Sector, SKU, Barcode/VIN, Brand, Parent Co, Subcategory)
- Physical BOM & Material Specs (Form Factor / Archetype, Primary Material, Mass, Closures/Interfaces, Barrier, Recycled %)
- Core Ingredients / Components & Origins (Raw Commodities, Origin Countries, Processing/Foundry Technology)
- Multi-Tier Supply Chain Routes (Tier 1 Converters, Tier 2 Smelters/Foundries, Tier 3 Mines/Farms, Maritime Lanes, Delays)
- Landed Cost Economics & Inflation (Wholesale, Retail/MSRP, Shock Landed Costs, Defended Costs, Savings)
- ESG & Regulatory Compliance (Scope 3 Carbon kg CO2e, EU PPWR/Battery Passport, Section 232/301 Tariffs)
"""

import os
import random
import pandas as pd
import numpy as np

def generate_grocery_catalog(output_path="data/grocery_catalog_5000.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    random.seed(42)
    np.random.seed(42)

    # ==========================================
    # SECTOR 1: Consumer Grocery & FMCG (5,000 SKUs)
    # ==========================================
    grocery_categories = {
        "Coffee & Tea": {
            "parent_cos": {
                "Davidoff": "Zino Davidoff Group (Tchibo GmbH)",
                "Nescafe": "Nestlé S.A.",
                "Illy": "illycaffè S.p.A.",
                "Lavazza": "Luigi Lavazza S.p.A.",
                "Starbucks": "Nestlé Global Coffee Alliance",
                "Twinings": "Associated British Foods plc",
                "Lipton": "LIPTON Teas and Infusions",
                "Tata Tea": "Tata Consumer Products Ltd",
                "Blue Tokai": "Blue Tokai Coffee Roasters",
                "Tim Hortons": "Restaurant Brands International"
            },
            "subcategories": ["Freeze-Dried Instant Coffee", "Dark Roast Whole Bean", "Single-Origin Filter Roast", "Nitro Cold Brew RTD", "Black & Green Specialty Tea"],
            "variants": ["Espresso 57 Intense", "Rich Aroma", "Fine Aroma", "Crema Intense", "Gold Blend", "Dark Roast Arabica", "Single Origin Colombian", "Earl Grey Leaf", "English Breakfast", "Green Tea Matcha"],
            "formats": [
                {
                    "fmt": "100g Instant Glass Jar", "net": "100g", "shelf_life": 730,
                    "archetype": "GLASS JAR", "pkg_mass": 230.0,
                    "container_mat": "Soda-Lime Flint Glass (Type III)",
                    "closure": "58mm Aromaseal Polypropylene Screw Cap", "closure_mass": 14.5,
                    "barrier": "Tamper-Evident Induction Heat Seal (Alu/PE)",
                    "recycled_pct": 38.0, "recyclability": "100% Infinitely Recyclable (Class A)",
                    "raw_mat": "100% High-Grown Central/South American Green Arabica",
                    "origin": "Colombia / Ethiopia / Brazil", "processing": "Cryogenic Sublimation (Freeze-Drying)",
                    "tier1": "Verallia European Glassworks (Essen, Germany)", "tier1_reg": "Central Europe",
                    "tier2": "Cryo-Drying & Roasting Facility (Bremen)", "tier2_reg": "Northern Europe",
                    "tier3": "Antioquia & Sidama Smallholder Cooperatives", "tier3_reg": "Latin America / East Africa",
                    "chokepoints": "Bab el-Mandeb / Red Sea", "lane": "Indian Ocean to Mediterranean via Suez (Detour to Cape)", "delay": 14,
                    "vuln": "Bab el-Mandeb / Red Sea green bean detour (+14 days)",
                    "retail": 8.95, "wholesale": 5.40, "pkg_base": 0.48, "raw_base": 2.60, "freight_base": 0.22,
                    "carbon": 0.34, "ppwr": "Compliant (Reusable/Recyclable)", "tariff": False
                },
                {
                    "fmt": "200g Instant Glass Jar", "net": "200g", "shelf_life": 730,
                    "archetype": "GLASS JAR", "pkg_mass": 340.0,
                    "container_mat": "Soda-Lime Flint Glass (Type III)",
                    "closure": "63mm Aromaseal Polypropylene Screw Cap", "closure_mass": 16.5,
                    "barrier": "Tamper-Evident Induction Heat Seal (Alu/PE)",
                    "recycled_pct": 38.0, "recyclability": "100% Infinitely Recyclable (Class A)",
                    "raw_mat": "100% Premium Arabica & High-Altitude Robusta Blend",
                    "origin": "Brazil / Vietnam / India", "processing": "Cryogenic Sublimation (Freeze-Drying)",
                    "tier1": "Owens-Illinois Container Glass (Lyon, France)", "tier1_reg": "Western Europe",
                    "tier2": "Central European Cryo Roasting & Annealing", "tier2_reg": "Western Europe",
                    "tier3": "Minas Gerais & Karnataka Coffee Plantations", "tier3_reg": "South America / South Asia",
                    "chokepoints": "Bab el-Mandeb / Red Sea", "lane": "Asia-to-Europe via Suez (Detour to Cape)", "delay": 14,
                    "vuln": "Bab el-Mandeb / Red Sea green bean detour (+14 days)",
                    "retail": 14.50, "wholesale": 8.80, "pkg_base": 0.62, "raw_base": 4.50, "freight_base": 0.34,
                    "carbon": 0.48, "ppwr": "Compliant (Reusable/Recyclable)", "tariff": False
                },
                {
                    "fmt": "250ml Nitro Cold Brew Slim Can", "net": "250ml", "shelf_life": 270,
                    "archetype": "SLIM CAN", "pkg_mass": 11.5,
                    "container_mat": "AA 3104 Cold-Rolled Aluminum Sheet",
                    "closure": "AA 5182 200-Diameter Stay-on-Tab End", "closure_mass": 1.3,
                    "barrier": "Water-based Epoxy-Phenolic Internal Lacquer",
                    "recycled_pct": 73.0, "recyclability": "100% Infinitely Recyclable (Class A)",
                    "raw_mat": "Steeped Arabica Cold Brew Extract + Liquid Nitrogen Dose",
                    "origin": "Brazil / Colombia", "processing": "Continuous Cold Extraction & In-line Nitrogen Dosing",
                    "tier1": "Ball Corporation Can Plant (Oss, Netherlands)", "tier1_reg": "Western Europe",
                    "tier2": "Alba / EGA Smelters (Bahrain / UAE)", "tier2_reg": "Middle East / Gulf",
                    "tier3": "Bauxite Refining (Guinea / Australia)", "tier3_reg": "West Africa / Oceania",
                    "chokepoints": "Strait of Hormuz", "lane": "Persian Gulf to Rotterdam Ocean Lane", "delay": 12,
                    "vuln": "Strait of Hormuz primary aluminum ingot supply",
                    "retail": 2.95, "wholesale": 1.65, "pkg_base": 0.118, "raw_base": 0.320, "freight_base": 0.018,
                    "carbon": 0.11, "ppwr": "Compliant (High-Recycled Standard)", "tariff": True
                },
                {
                    "fmt": "500g Whole Bean Vacuum Foil", "net": "500g", "shelf_life": 540,
                    "archetype": "MULTI-FOIL POUCH", "pkg_mass": 18.0,
                    "container_mat": "PET/ALU/PE Triplex Barrier Laminate",
                    "closure": "One-Way Degassing Aroma Valve (PP/Silicone)", "closure_mass": 1.2,
                    "barrier": "High-Barrier 7-Micron Foil Layer (OTR < 0.1)",
                    "recycled_pct": 12.0, "recyclability": "Specialized Industrial Facility (Class C)",
                    "raw_mat": "100% Specialty Arabica Roasted Whole Beans",
                    "origin": "Colombia / Guatemala / Rwanda", "processing": "Convection Drum Roasting & Inert Nitrogen Flushing",
                    "tier1": "Amcor Flexibles (Gent, Belgium)", "tier1_reg": "Western Europe",
                    "tier2": "High-Purity Aluminum Thin-Foil Rolling (Germany)", "tier2_reg": "Central Europe",
                    "tier3": "Direct-Trade Specialty Estates", "tier3_reg": "Latin America / East Africa",
                    "chokepoints": "Cape of Good Hope", "lane": "East Africa to European Ports via Cape", "delay": 10,
                    "vuln": "Cape of Good Hope detour on African shipping",
                    "retail": 12.90, "wholesale": 7.80, "pkg_base": 0.32, "raw_base": 4.80, "freight_base": 0.28,
                    "carbon": 0.19, "ppwr": "Transition Risk (Multilayer Barrier)", "tariff": False
                }
            ]
        },
        "Beverages & Sodas": {
            "parent_cos": {
                "Coca-Cola": "The Coca-Cola Company",
                "Diet Coke": "The Coca-Cola Company",
                "Pepsi": "PepsiCo, Inc.",
                "Pepsi Black": "PepsiCo, Inc.",
                "Red Bull": "Red Bull GmbH",
                "Monster Energy": "Monster Beverage Corporation",
                "Sprite": "The Coca-Cola Company",
                "Fanta": "The Coca-Cola Company",
                "San Pellegrino": "Sanpellegrino S.p.A. (Nestlé)",
                "Schweppes": "Suntory Beverage & Food Ltd"
            },
            "subcategories": ["Carbonated Soft Drink", "Functional Energy Drink", "Sparkling Mineral Water", "Flavored Mixer & Tonic", "Zero Sugar Soda"],
            "variants": ["Classic", "Zero Sugar", "Cherry", "Lime", "Sugarfree Energy", "Original Energy", "Tropical Splash", "Tonic Water", "Sparkling Citrus", "Ginger Ale"],
            "formats": [
                {
                    "fmt": "330ml Standard Aluminum Can", "net": "330ml", "shelf_life": 365,
                    "archetype": "ALUMINUM CAN", "pkg_mass": 13.0,
                    "container_mat": "AA 3104 Cold-Rolled Coil Sheet",
                    "closure": "AA 5182 202-Diameter Easy-Open Stay-on-Tab End", "closure_mass": 1.5,
                    "barrier": "BPA-NI Polymer Dispersion Internal Coating",
                    "recycled_pct": 74.0, "recyclability": "100% Infinitely Recyclable (Class A)",
                    "raw_mat": "Carbonated Water, High-Fructose Corn Syrup/Sweeteners, Acidulants",
                    "origin": "Domestic / Nearshore Bottling Hub", "processing": "Continuous High-Speed D&I Can Line (2,000 cpm)",
                    "tier1": "Crown Holdings Beverage Packaging (Parma, Italy)", "tier1_reg": "Southern Europe",
                    "tier2": "Alba Smelter (Askar, Bahrain)", "tier2_reg": "Middle East / Gulf",
                    "tier3": "Bauxite Mining & Calcined Alumina Refining", "tier3_reg": "Guinea / Australia",
                    "chokepoints": "Strait of Hormuz", "lane": "Gulf Smelters to Antwerp/Rotterdam", "delay": 14,
                    "vuln": "Strait of Hormuz primary aluminum ingot supply",
                    "retail": 1.50, "wholesale": 0.85, "pkg_base": 0.125, "raw_base": 0.085, "freight_base": 0.015,
                    "carbon": 0.12, "ppwr": "Compliant (High-Recycled Standard)", "tariff": True
                },
                {
                    "fmt": "250ml Slimline Can", "net": "250ml", "shelf_life": 365,
                    "archetype": "SLIM CAN", "pkg_mass": 11.5,
                    "container_mat": "AA 3104 Cold-Rolled Aluminum Sheet",
                    "closure": "AA 5182 200-Diameter Colored Stay-on-Tab", "closure_mass": 1.3,
                    "barrier": "Water-based Epoxy Internal Lacquer",
                    "recycled_pct": 72.0, "recyclability": "100% Infinitely Recyclable (Class A)",
                    "raw_mat": "Taurine, Caffeine, B-Vitamins, Carbonated Water Base",
                    "origin": "Austria / Switzerland", "processing": "Specialized Slim D&I Line with Digital Printing",
                    "tier1": "Rexam/Ball Packaging (Widnau, Switzerland)", "tier1_reg": "Central Europe",
                    "tier2": "Emirates Global Aluminium (Jebel Ali, UAE)", "tier2_reg": "Middle East / Gulf",
                    "tier3": "Australian Alumina Refineries", "tier3_reg": "Oceania",
                    "chokepoints": "Strait of Hormuz", "lane": "Persian Gulf to Mediterranean", "delay": 12,
                    "vuln": "Strait of Hormuz primary aluminum ingot supply",
                    "retail": 2.50, "wholesale": 1.35, "pkg_base": 0.115, "raw_base": 0.220, "freight_base": 0.016,
                    "carbon": 0.11, "ppwr": "Compliant (High-Recycled Standard)", "tariff": True
                }
            ]
        },
        "Condiments & Sauces": {
            "parent_cos": {
                "Heinz": "The Kraft Heinz Company",
                "Hellmann's": "Unilever plc",
                "Barilla": "Barilla Holding S.p.A.",
                "Maggi": "Nestlé S.A.",
                "Kikkoman": "Kikkoman Corporation",
                "Tabasco": "McIlhenny Company"
            },
            "subcategories": ["Table Sauce & Ketchup", "Mayonnaise & Emulsions", "Pasta Sauce & Passata", "Hot Chilli & Pepper Sauce"],
            "variants": ["Tomato Ketchup Top-Down", "Real Mayonnaise", "Basilico Pasta Sauce", "Hot Chilli Sauce", "Naturally Brewed Soy Sauce"],
            "formats": [
                {
                    "fmt": "400ml Squeeze Bottle", "net": "400ml", "shelf_life": 365,
                    "archetype": "PET SQUEEZE BOTTLE", "pkg_mass": 34.0,
                    "container_mat": "Multilayer PET with EVOH Oxygen Scavenger Layer",
                    "closure": "38-400 PP Flip-Top with Silicone Slit Valve", "closure_mass": 6.5,
                    "barrier": "EVOH Middle Layer (Oxygen Transmission Rate < 0.2)",
                    "recycled_pct": 25.0, "recyclability": "Kerbside Recyclable (Class B)",
                    "raw_mat": "Tomato Paste (32° Brix), Distilled Vinegar, Cane Sugar, Salt",
                    "origin": "California & Southern Europe (Extremadura/Po Valley)", "processing": "Vacuum Evaporation & High-Shear Emulsification",
                    "tier1": "AptarGroup Dispensing Systems (Crystal Lake, IL)", "tier1_reg": "North America / Europe",
                    "tier2": "LyondellBasell / Ineos Polyolefins Refining", "tier2_reg": "Western Europe",
                    "tier3": "Industrial Tomato Processing Farms", "tier3_reg": "Mediterranean / California",
                    "chokepoints": "Bab el-Mandeb / Red Sea", "lane": "Trans-Mediterranean to Global Bottling Centers", "delay": 12,
                    "vuln": "Mediterranean crop drought + Red Sea freight",
                    "retail": 3.49, "wholesale": 1.95, "pkg_base": 0.180, "raw_base": 0.520, "freight_base": 0.060,
                    "carbon": 0.18, "ppwr": "Transition Risk (Multilayer Barrier)", "tariff": False
                },
                {
                    "fmt": "500g Glass Jar", "net": "500g", "shelf_life": 730,
                    "archetype": "GLASS JAR", "pkg_mass": 260.0,
                    "container_mat": "Soda-Lime Flint Glass (Type III)",
                    "closure": "63mm Tinplate Twist-Off Lug Cap with Plastisol Compound", "closure_mass": 11.2,
                    "barrier": "Vitreous Glass Wall + Hermetic Vacuum Lug Seal",
                    "recycled_pct": 42.0, "recyclability": "100% Infinitely Recyclable (Class A)",
                    "raw_mat": "Crushed Diced Tomatoes, Extra Virgin Olive Oil, Fresh Basil",
                    "origin": "Parma, Italy / Po Valley", "processing": "Thermal Pasteurization & Hot-Fill Vacuum Capping",
                    "tier1": "Bormioli Luigi Glassworks (Parma, Italy)", "tier1_reg": "Southern Europe",
                    "tier2": "European Electrolytic Tinplate Steel Mills", "tier2_reg": "Central Europe",
                    "tier3": "Italian Controlled Agronomic Supply Chains", "tier3_reg": "Southern Europe",
                    "chokepoints": "Bab el-Mandeb / Red Sea", "lane": "Mediterranean Shipping Corridors", "delay": 10,
                    "vuln": "Mediterranean crop drought + Red Sea freight",
                    "retail": 4.20, "wholesale": 2.40, "pkg_base": 0.380, "raw_base": 0.850, "freight_base": 0.080,
                    "carbon": 0.36, "ppwr": "Compliant (Infinitely Recyclable)", "tariff": False
                }
            ]
        },
        "Edible Oils & Fats": {
            "parent_cos": {
                "Filippo Berio": "SALOV S.p.A.",
                "Bertolli": "Deoleo S.A.",
                "De Cecco": "F.lli De Cecco di Filippo Fara San Martino S.p.A.",
                "Borges": "Borges Agricultural & Industrial Edible Oils"
            },
            "subcategories": ["Extra Virgin Olive Oil (EVOO)", "Pure & Light Olive Oil", "Cold-Pressed Seed Oil"],
            "variants": ["Extra Virgin Olive Oil", "Pure Olive Oil", "Cold Pressed Extra Light"],
            "formats": [
                {
                    "fmt": "500ml Marasca Glass Bottle", "net": "500ml", "shelf_life": 540,
                    "archetype": "GLASS BOTTLE", "pkg_mass": 310.0,
                    "container_mat": "UVAG Dark Green Tint Soda-Lime Glass (Type III)",
                    "closure": "31.5mm Aluminum ROPP Cap with Polyethylene Pourer", "closure_mass": 4.2,
                    "barrier": "UVAG Light Barrier (Blocks > 95% of UV 290-400nm)",
                    "recycled_pct": 65.0, "recyclability": "100% Infinitely Recyclable (Class A)",
                    "raw_mat": "100% Cold-Pressed Extra Virgin Olive Oil (Acidity < 0.3%)",
                    "origin": "Andalusia, Spain / Peloponnese, Greece", "processing": "Continuous Cold Centrifugal Decanter Extraction (< 27°C)",
                    "tier1": "Vidrala Glass Containers (Llodio, Spain)", "tier1_reg": "Southern Europe",
                    "tier2": "Guala Closures Non-Refillable Pourers (Spinetta Marengo)", "tier2_reg": "Southern Europe",
                    "tier3": "Jaén & Kalamata Olive Farming Cooperatives", "tier3_reg": "Mediterranean Basin",
                    "chokepoints": "Bab el-Mandeb / Red Sea", "lane": "Mediterranean to Transatlantic & Asian Hubs", "delay": 14,
                    "vuln": "Southern Europe harvest collapse (-35% yield)",
                    "retail": 9.50, "wholesale": 6.10, "pkg_base": 0.380, "raw_base": 3.400, "freight_base": 0.180,
                    "carbon": 0.42, "ppwr": "Compliant (Infinitely Recyclable)", "tariff": False
                }
            ]
        },
        "Dairy & Plant Alternatives": {
            "parent_cos": {
                "Oatly": "Oatly Group AB",
                "Alpro": "Danone S.A.",
                "Chobani": "Chobani, LLC",
                "Kerrygold": "Ornua Co-operative Limited"
            },
            "subcategories": ["Barista Plant-Based Milk", "Organic Dairy & Butter", "Cultured Greek Yogurt"],
            "variants": ["Barista Edition Oat Milk", "Unsweetened Almond Milk", "Salted Pure Butter"],
            "formats": [
                {
                    "fmt": "1L Aseptic Carton", "net": "1000ml", "shelf_life": 365,
                    "archetype": "TETRAPAK", "pkg_mass": 28.5,
                    "container_mat": "Tetra Brik Aseptic (Paperboard 75%, PE 20%, Alu 5%)",
                    "closure": "HeliCap 23 Bio-based Polyethylene Screw Cap", "closure_mass": 4.2,
                    "barrier": "Ultra-thin 6.3-Micron Aluminum Foil Barrier (Light/O2 gas-tight)",
                    "recycled_pct": 20.0, "recyclability": "Specialized Hydrapulper Recyclable (Class B)",
                    "raw_mat": "Whole Grain Oats, Water, Rapeseed Oil, Dipotassium Phosphate",
                    "origin": "Sweden / Finland / Canada", "processing": "Enzymatic Liquefaction & Ultra-High Temperature (UHT) Aseptic Fill",
                    "tier1": "Tetra Pak Packaging Solutions (Lund, Sweden)", "tier1_reg": "Northern Europe",
                    "tier2": "Stora Enso Liquid Packaging Board Mills (Imatra)", "tier2_reg": "Northern Europe",
                    "tier3": "Nordic Oat Farming Cooperatives", "tier3_reg": "Northern Europe",
                    "chokepoints": "Cape of Good Hope", "lane": "Northern Europe to Global Outbound Lanes", "delay": 8,
                    "vuln": "Aseptic aluminum barrier foil supply pinch",
                    "retail": 3.20, "wholesale": 1.80, "pkg_base": 0.165, "raw_base": 0.520, "freight_base": 0.045,
                    "carbon": 0.14, "ppwr": "Compliant (FSC Certified Bio-Board)", "tariff": False
                }
            ]
        },
        "Snacks & Confectionery": {
            "parent_cos": {
                "Lindt": "Chocoladefabriken Lindt & Sprüngli AG",
                "Ferrero Rocher": "Ferrero International S.A.",
                "Cadbury": "Mondelēz International, Inc.",
                "Lay's": "PepsiCo, Inc."
            },
            "subcategories": ["Premium Swiss/Belgian Chocolate", "Savory Crisps & Tortillas"],
            "variants": ["Excellence 85% Cocoa Dark", "Classic Milk Chocolate", "Original Potato Crisps"],
            "formats": [
                {
                    "fmt": "100g Slim Bar Foil Pack", "net": "100g", "shelf_life": 365,
                    "archetype": "MULTI-FOIL POUCH", "pkg_mass": 6.5,
                    "container_mat": "Printed Aluminum Foil / BOPP Cold-Seal Wrap",
                    "closure": "Fin-Seal Cold-Seal Longitudinal Seam", "closure_mass": 0.0,
                    "barrier": "Hermetic Barrier against Fat Bloom & Moisture Absorption",
                    "recycled_pct": 15.0, "recyclability": "Kerbside Foil Recyclable (Class B)",
                    "raw_mat": "Cocoa Mass, Cocoa Butter, Demerara Sugar, Bourbon Vanilla",
                    "origin": "Ghana / Côte d'Ivoire / Ecuador", "processing": "72-Hour Longitudinal Conching & Precision Tempering",
                    "tier1": "Amcor Flexible Confectionery Packaging (Zurich)", "tier1_reg": "Central Europe",
                    "tier2": "Barry Callebaut Cacao Processing Mills (Wieze, Belgium)", "tier2_reg": "Western Europe",
                    "tier3": "West African Smallholder Cocoa Farms", "tier3_reg": "West Africa",
                    "chokepoints": "Cape of Good Hope", "lane": "Gulf of Guinea to European Atlantic Ports via Cape", "delay": 14,
                    "vuln": "West Africa cacao crop deficits (+200% bean cost)",
                    "retail": 3.80, "wholesale": 2.10, "pkg_base": 0.085, "raw_base": 1.250, "freight_base": 0.040,
                    "carbon": 0.16, "ppwr": "Compliant (Ultra-lightweight Foil)", "tariff": False
                }
            ]
        },
        "Cereals, Pasta & Grains": {
            "parent_cos": {
                "Barilla": "Barilla Holding S.p.A.",
                "De Cecco": "F.lli De Cecco di Filippo Fara San Martino S.p.A.",
                "Kellogg's": "Kellanova / WK Kellogg Co",
                "Tilda": "Ebro Foods, S.A."
            },
            "subcategories": ["Bronze-Cut Durum Wheat Pasta", "Single-Origin Basmati Rice"],
            "variants": ["Spaghetti No. 5 Durum Wheat", "Pure Basmati Rice"],
            "formats": [
                {
                    "fmt": "500g Blue Cardboard Box", "net": "500g", "shelf_life": 1095,
                    "archetype": "FOLDING CARTON", "pkg_mass": 22.0,
                    "container_mat": "100% Recycled Kraft Paperboard (GD2 Coated Duplex)",
                    "closure": "Adhesive Glue-Sealed Top & Bottom End-Flaps", "closure_mass": 0.5,
                    "barrier": "Breathable High-Rigidity Cellulose Matrix",
                    "recycled_pct": 100.0, "recyclability": "100% Infinitely Recyclable Paper (Class A)",
                    "raw_mat": "100% Selected High-Protein Italian Durum Wheat Semolina, Spring Water",
                    "origin": "Puglia, Italy / North Dakota, USA", "processing": "Slow Bronze-Die Extrusion & Low-Temp Drying",
                    "tier1": "Mayr-Melnhof Karton (Vienna, Austria)", "tier1_reg": "Central Europe",
                    "tier2": "Semolina Semolerie Industrial Mills (Foggia)", "tier2_reg": "Southern Europe",
                    "tier3": "Durum Wheat Agricultural Producers", "tier3_reg": "Mediterranean / North America",
                    "chokepoints": "Black Sea Corridor", "lane": "Black Sea Grain to Mediterranean Milling Corridors", "delay": 12,
                    "vuln": "Global durum wheat milling capacity bottlenecks",
                    "retail": 2.20, "wholesale": 1.15, "pkg_base": 0.085, "raw_base": 0.450, "freight_base": 0.035,
                    "carbon": 0.11, "ppwr": "Compliant (100% Recycled Fiber)", "tariff": False
                }
            ]
        }
    }

    all_records = []
    item_id = 10001
    g_keys = list(grocery_categories.keys())

    # 1. Generate 5,000 Grocery Items
    while len(all_records) < 5000:
        c_name = g_keys[len(all_records) % len(g_keys)]
        c_data = grocery_categories[c_name]
        brand = random.choice(list(c_data["parent_cos"].keys()))
        parent_co = c_data["parent_cos"][brand]
        variant = random.choice(c_data["variants"])
        subcat = random.choice(c_data["subcategories"])
        fmt_spec = random.choice(c_data["formats"])

        jitter = round(random.uniform(0.92, 1.18), 2)
        retail_p = round(fmt_spec["retail"] * jitter, 2)
        wholesale_p = round(fmt_spec["wholesale"] * jitter, 2)
        pkg_base = round(fmt_spec["pkg_base"] * jitter, 3)
        raw_base = round(fmt_spec["raw_base"] * jitter, 3)
        freight_base = round(fmt_spec["freight_base"] * jitter, 3)

        shock_mult = random.uniform(1.55, 1.85)
        pkg_shock = round(pkg_base * shock_mult, 3)
        freight_shock = round(freight_base * 2.8, 3)
        unmitigated_retail = round(retail_p + (pkg_shock - pkg_base) * 1.85 + (freight_shock - freight_base), 2)
        defended_retail = round(retail_p + (pkg_shock - pkg_base) * 0.35, 2)
        savings = round(unmitigated_retail - defended_retail, 2)

        ean = f"89010{item_id:07d}"[:13]
        title = f"{brand} {variant} ({fmt_spec['fmt']})"

        all_records.append({
            "sector": "Consumer Grocery & FMCG",
            "sku_id": f"SKU-{item_id}",
            "gtin_barcode": ean,
            "product_name": title,
            "brand": brand,
            "parent_company": parent_co,
            "category": c_name,
            "subcategory": subcat,
            "net_weight_volume": fmt_spec["net"],
            "shelf_life_days": fmt_spec["shelf_life"],
            "container_archetype": fmt_spec["archetype"],
            "primary_container_material": fmt_spec["container_mat"],
            "packaging_mass_grams": fmt_spec["pkg_mass"],
            "closure_type": fmt_spec["closure"],
            "closure_mass_grams": fmt_spec["closure_mass"],
            "seal_liner_barrier": fmt_spec["barrier"],
            "recycled_content_pct": fmt_spec["recycled_pct"],
            "recyclability_class": fmt_spec["recyclability"],
            "primary_raw_materials": fmt_spec["raw_mat"],
            "raw_material_origin_country": fmt_spec["origin"],
            "processing_technology": fmt_spec["processing"],
            "tier1_converter": fmt_spec["tier1"],
            "tier1_converter_region": fmt_spec["tier1_reg"],
            "tier2_processor_region": fmt_spec["tier2_reg"],
            "tier3_origin_region": fmt_spec["tier3_reg"],
            "critical_chokepoints": fmt_spec["chokepoints"],
            "shipping_lane_exposure": fmt_spec["lane"],
            "cape_detour_transit_delay_days": fmt_spec["delay"],
            "primary_chokepoint_vulnerability": fmt_spec["vuln"],
            "wholesale_price_usd": wholesale_p,
            "retail_price_usd": retail_p,
            "packaging_baseline_cost_usd": pkg_base,
            "raw_content_cost_usd": raw_base,
            "freight_baseline_usd": freight_base,
            "unmitigated_shock_packaging_cost_usd": pkg_shock,
            "unmitigated_retail_shelf_price_usd": unmitigated_retail,
            "basketshield_defended_shelf_price_usd": defended_retail,
            "consumer_savings_per_unit_usd": savings,
            "gross_margin_pct": round(((retail_p - wholesale_p) / retail_p) * 100.0, 1),
            "scope3_packaging_carbon_kg_co2e": fmt_spec["carbon"],
            "eu_ppwr_status": fmt_spec["ppwr"],
            "section_232_tariff_applies": fmt_spec["tariff"]
        })
        item_id += 1

    # ==========================================
    # SECTOR 2: Consumer Electronics & Computing (500 SKUs)
    # ==========================================
    electronics_templates = [
        {
            "brand": "Apple", "parent": "Apple Inc.", "subcat": "Flagship Smartphone",
            "name": "Apple iPhone 16 Pro (256GB Titanium Chassis)", "archetype": "SMARTPHONE UNIBODY",
            "mass": 199.0, "mat": "Grade 5 Titanium / Recycled Aluminum Subframe",
            "closure": "Ceramic Shield 2nd Gen + Sapphire Glass Lens Ring", "closure_mass": 28.0,
            "barrier": "IP68 Hermetic Nano-Sealing Gasket (0.01mm)", "recycled": 100.0, "recyc_cls": "Advanced Closed-Loop Daisy Disassembly (Class A)",
            "raw": "Apple A18 Pro 3nm Silicon Die, 8GB LPDDR5X-7500 DRAM (SK Hynix/Micron), Recycled Cobalt", "origin": "Taiwan / South Korea / USA / China",
            "proc": "TSMC N3E 3nm Lithography + InFO-PoP (Integrated Fan-Out Package-on-Package)", "tier1": "Foxconn Technology Group (Zhengzhou, China)", "tier1_reg": "East Asia",
            "tier2": "TSMC Advanced Packaging GigaFab & SK Hynix DRAM Lines", "tier2_reg": "East Asia (Taiwan / South Korea)",
            "tier3": "SK Hynix 1b-nm DRAM Fab & Catamarca Lithium Brines", "tier3_reg": "South Korea / South America",
            "choke": "Taiwan Strait", "lane": "Taiwan Strait to Transpacific Air & Ocean Freight", "delay": 21,
            "vuln": "AI data center HBM3e wafer crowding out consumer LPDDR5X memory (+45% DRAM spot surge) & TSMC packaging bottlenecks",
            "retail": 999.00, "wholesale": 540.00, "pkg_base": 68.00, "raw_base": 340.00, "freight_base": 14.50,
            "carbon": 61.0, "ppwr": "Compliant (Circular Daisy Recovery)", "tariff": True
        },
        {
            "brand": "NVIDIA", "parent": "NVIDIA Corporation", "subcat": "Data Center AI Accelerator",
            "name": "NVIDIA H100 Tensor Core GPU (80GB SXM5 Accelerator)", "archetype": "GPU PCIE ACCELERATOR",
            "mass": 2150.0, "mat": "Megtron-7 Multilayer PCB + Copper Vapor Chamber",
            "closure": "Die-Cast Cold-Forged Aluminum Retention Bracket", "closure_mass": 180.0,
            "barrier": "Sintered Micro-Capillary Vapor Chamber Vacuum Seal", "recycled": 45.0, "recyc_cls": "Industrial Electronic Scrap Recovery (Class B)",
            "raw": "GH100 4N Silicon Die, 80GB HBM3 Stacks (SK Hynix 24GB 8-Hi TSV), OFHC Copper", "origin": "Taiwan / South Korea / USA",
            "proc": "TSMC CoWoS-S (Chip-on-Wafer-on-Substrate) 2.5D Packaging", "tier1": "Wistron / Foxconn Industrial Internet (Hsinchu, Taiwan)", "tier1_reg": "East Asia (Taiwan)",
            "tier2": "TSMC Advanced Packaging Fab 6 (Zhunan, Taiwan)", "tier2_reg": "East Asia (Taiwan)",
            "tier3": "SK Hynix HBM3 Fab (Icheon, South Korea)", "tier3_reg": "East Asia (Korea)",
            "choke": "Taiwan Strait", "lane": "East Asian Semiconductor Air Bridge to Global Cloud Hubs", "delay": 28,
            "vuln": "Hyperscaler GenAI demand consuming 85%+ of global HBM3e capacity & TSMC CoWoS substrate allocation squeeze",
            "retail": 32000.00, "wholesale": 14500.00, "pkg_base": 650.00, "raw_base": 8400.00, "freight_base": 120.00,
            "carbon": 280.0, "ppwr": "Exempt (Enterprise Capital Equipment)", "tariff": True
        },
        {
            "brand": "Apple", "parent": "Apple Inc.", "subcat": "High-Performance Laptop",
            "name": "Apple MacBook Pro 16\" (M3 Max, 36GB RAM, Space Black)", "archetype": "LAPTOP ENCLOSURE",
            "mass": 2140.0, "mat": "100% Recycled 6000-Series Unibody Aluminum",
            "closure": "Anodized Hinge Assembly with Liquid Crystal Display Bezel", "closure_mass": 320.0,
            "barrier": "Space Black Anodization (Dual-Layer Anti-Fingerprint Oxide)", "recycled": 100.0, "recyc_cls": "100% Closed-Loop Recycled Aluminum (Class A)",
            "raw": "Apple M3 Max 3nm SoC, 36GB Unified LPDDR5X Subsystem (Micron/SK Hynix), Mini-LED Backlight", "origin": "Taiwan / Japan / South Korea",
            "proc": "Subtractive 5-Axis CNC Precision Monocoque Milling + On-Package Memory Stacking", "tier1": "Quanta Computer (Shanghai, China)", "tier1_reg": "East Asia",
            "tier2": "TSMC 3nm GigaFab (Tainan, Taiwan)", "tier2_reg": "East Asia (Taiwan)",
            "tier3": "Micron/SK Hynix Leading-Edge 1b DRAM Lines (Hiroshima/Icheon)", "tier3_reg": "East Asia",
            "choke": "Taiwan Strait", "lane": "Shanghai / Taipei Intermodal Express Lanes", "delay": 18,
            "vuln": "AI data center demand crowding out high-density unified DRAM packages (+52% memory inflation) & TSMC wafer surcharges",
            "retail": 3499.00, "wholesale": 2100.00, "pkg_base": 145.00, "raw_base": 1250.00, "freight_base": 32.00,
            "carbon": 145.0, "ppwr": "Compliant (Mono-alloy Aluminum)", "tariff": True
        },
        {
            "brand": "Samsung", "parent": "Samsung Electronics Co., Ltd.", "subcat": "Android Flagship Smartphone",
            "name": "Samsung Galaxy S24 Ultra (512GB Titanium Gray)", "archetype": "SMARTPHONE UNIBODY",
            "mass": 232.0, "mat": "Aerospace Titanium Edge Frame + Armor Aluminum Midframe",
            "closure": "Corning Gorilla Armor Optical Anti-Reflective Cover Glass", "closure_mass": 32.0,
            "barrier": "IP68 Micro-Dispensed Polyurethane Gasket", "recycled": 50.0, "recyc_cls": "Advanced Electronic Recycling (Class A)",
            "raw": "Snapdragon 8 Gen 3 (TSMC 4N), 12GB LPDDR5X DRAM (Samsung 1b-nm), Dynamic AMOLED 2X", "origin": "Taiwan / South Korea / Vietnam",
            "proc": "Precision Titanium Cold Forging & 1b-nm DRAM Lithography", "tier1": "Samsung Electronics Thai Nguyen (SEVT, Vietnam)", "tier1_reg": "Southeast Asia",
            "tier2": "Samsung Electronics Pyeongtaek Memory Complex (Line 3/4)", "tier2_reg": "East Asia (Korea)",
            "tier3": "Samsung Wafer Fabrication & Corning Display Substrates", "tier3_reg": "East Asia",
            "choke": "South China Sea", "lane": "Vietnam / South China Sea to Global Air Hubs", "delay": 14,
            "vuln": "Samsung DRAM wafer capacity shifted to HBM3e server lines, causing +42% consumer LPDDR5X spot price inflation",
            "retail": 1299.00, "wholesale": 680.00, "pkg_base": 72.00, "raw_base": 420.00, "freight_base": 16.00,
            "carbon": 68.0, "ppwr": "Compliant (Recycled Rare Minerals)", "tariff": False
        },
        {
            "brand": "Sony", "parent": "Sony Group Corporation", "subcat": "Gaming Entertainment System",
            "name": "Sony PlayStation 5 Pro (2TB Custom AMD SoC)", "archetype": "GAME CONSOLE CHASSIS",
            "mass": 3100.0, "mat": "Injection-Molded Polycarbonate Shell + Die-Cast Heatsink",
            "closure": "Modular Removable Faceplates with Custom Texture", "closure_mass": 450.0,
            "barrier": "Liquid Metal (Gallium-Indium) Thermal Interface Seal", "recycled": 35.0, "recyc_cls": "WEEE Compliant Consumer Electronics (Class B)",
            "raw": "Custom AMD RDNA3/Zen2 4nm APU, 16GB GDDR6 High-Speed VRAM (Micron), 2TB Custom NVMe", "origin": "Taiwan / Japan / Malaysia",
            "proc": "Surface Mount Technology (SMT) Automated Assembly", "tier1": "Foxconn Yantai & Kisarazu Automated Plant", "tier1_reg": "East Asia",
            "tier2": "TSMC Fab 18 (Tainan, Taiwan)", "tier2_reg": "East Asia (Taiwan)",
            "tier3": "Micron Hiroshima DRAM Fab (GDDR6 Production Lines)", "tier3_reg": "East Asia (Japan)",
            "choke": "Taiwan Strait", "lane": "East Asian Container Ports to Long Beach / Rotterdam", "delay": 16,
            "vuln": "AI GPU memory demand cannibalizing Micron/Samsung GDDR6 capacity (+38% VRAM surge) & Taiwan Strait transit risks",
            "retail": 699.00, "wholesale": 480.00, "pkg_base": 55.00, "raw_base": 310.00, "freight_base": 24.00,
            "carbon": 110.0, "ppwr": "Compliant (EU WEEE Directive)", "tariff": True
        }
    ]

    while len(all_records) < 5500:
        tpl = random.choice(electronics_templates)
        jitter = round(random.uniform(0.95, 1.12), 2)
        retail_p = round(tpl["retail"] * jitter, 2)
        wholesale_p = round(tpl["wholesale"] * jitter, 2)
        pkg_base = round(tpl["pkg_base"] * jitter, 2)
        raw_base = round(tpl["raw_base"] * jitter, 2)
        freight_base = round(tpl["freight_base"] * jitter, 2)

        shock_mult = random.uniform(1.35, 1.65)
        pkg_shock = round(pkg_base * shock_mult, 2)
        freight_shock = round(freight_base * 2.4, 2)
        unmitigated_retail = round(retail_p + (pkg_shock - pkg_base) * 1.5 + (freight_shock - freight_base), 2)
        defended_retail = round(retail_p + (pkg_shock - pkg_base) * 0.25, 2)
        savings = round(unmitigated_retail - defended_retail, 2)

        upc = f"01959{item_id:07d}"[:13]

        all_records.append({
            "sector": "Consumer Electronics & Computing",
            "sku_id": f"SKU-{item_id}",
            "gtin_barcode": upc,
            "product_name": tpl["name"],
            "brand": tpl["brand"],
            "parent_company": tpl["parent"],
            "category": "Consumer Electronics",
            "subcategory": tpl["subcat"],
            "net_weight_volume": f"{tpl['mass']:.0f}g",
            "shelf_life_days": 1825,
            "container_archetype": tpl["archetype"],
            "primary_container_material": tpl["mat"],
            "packaging_mass_grams": tpl["mass"],
            "closure_type": tpl["closure"],
            "closure_mass_grams": tpl["closure_mass"],
            "seal_liner_barrier": tpl["barrier"],
            "recycled_content_pct": tpl["recycled"],
            "recyclability_class": tpl["recyc_cls"],
            "primary_raw_materials": tpl["raw"],
            "raw_material_origin_country": tpl["origin"],
            "processing_technology": tpl["proc"],
            "tier1_converter": tpl["tier1"],
            "tier1_converter_region": tpl["tier1_reg"],
            "tier2_processor_region": tpl["tier2_reg"],
            "tier3_origin_region": tpl["tier3_reg"],
            "critical_chokepoints": tpl["choke"],
            "shipping_lane_exposure": tpl["lane"],
            "cape_detour_transit_delay_days": tpl["delay"],
            "primary_chokepoint_vulnerability": tpl["vuln"],
            "wholesale_price_usd": wholesale_p,
            "retail_price_usd": retail_p,
            "packaging_baseline_cost_usd": pkg_base,
            "raw_content_cost_usd": raw_base,
            "freight_baseline_usd": freight_base,
            "unmitigated_shock_packaging_cost_usd": pkg_shock,
            "unmitigated_retail_shelf_price_usd": unmitigated_retail,
            "basketshield_defended_shelf_price_usd": defended_retail,
            "consumer_savings_per_unit_usd": savings,
            "gross_margin_pct": round(((retail_p - wholesale_p) / retail_p) * 100.0, 1),
            "scope3_packaging_carbon_kg_co2e": tpl["carbon"],
            "eu_ppwr_status": tpl["ppwr"],
            "section_232_tariff_applies": tpl["tariff"]
        })
        item_id += 1

    # ==========================================
    # SECTOR 3: Electric Vehicles & Automotive (500 SKUs)
    # ==========================================
    ev_templates = [
        {
            "brand": "Tesla", "parent": "Tesla, Inc.", "subcat": "Compact Executive EV Sedan",
            "name": "Tesla Model 3 Highland Long Range AWD (78.1kWh NMC Pack)", "archetype": "EV SKATEBOARD CHASSIS",
            "mass": 485000.0, "mat": "High-Pressure Gigacast AlSi10Mn Aluminum + Ultra-High Strength Steel",
            "closure": "Front/Rear Integrated Die-Cast Subframes with Structural Pack", "closure_mass": 142000.0,
            "barrier": "Intumescent Aerogel Thermal Runaway Fire Barrier (UL94 V-0)", "recycled": 42.0, "recyc_cls": "Circular Battery Hydro-metallurgical Recycling (Class A)",
            "raw": "NMC 811 Cylindrical Battery Cells, Silicon Carbide (SiC) Inverters, NdFeB Drive Motors", "origin": "USA / Japan / Chile / Australia",
            "proc": "6,000-Tonne Giga Press Injection + Automated Cell Module Stacking", "tier1": "Tesla Gigafactory Texas / Berlin / Shanghai", "tier1_reg": "North America / Europe / China",
            "tier2": "Panasonic / CATL Battery Cell Manufacturing (Niigata / Ningde)", "tier2_reg": "East Asia",
            "tier3": "Albemarle Lithium Brines (Atacama) & Vale Class-1 Nickel", "tier3_reg": "South America / Canada",
            "choke": "Malacca Strait", "lane": "Australia/Chile Spodumene to Asian Precursor Refineries", "delay": 21,
            "vuln": "Malacca Strait refined battery precursor shipping backlogs & Chinese synthetic graphite export controls",
            "retail": 42490.00, "wholesale": 28500.00, "pkg_base": 12400.00, "raw_base": 8200.00, "freight_base": 950.00,
            "carbon": 8200.0, "ppwr": "Compliant (EU Battery Passport 2026)", "tariff": True
        },
        {
            "brand": "Tesla", "parent": "Tesla, Inc.", "subcat": "Full-Size Electric Pickup Truck",
            "name": "Tesla Cybertruck Dual Motor AWD (123kWh 4680 Structural Pack)", "archetype": "4680 CYLINDRICAL PACK",
            "mass": 780000.0, "mat": "Ultra-Hard 30X Cold-Rolled Stainless Steel Exoskeleton (HFS)",
            "closure": "Armor Glass Acoustic Laminated Windshield + Powered Tonneau", "closure_mass": 165000.0,
            "barrier": "Structural Polyurethane Potting Foam & Cold-Rolled Steel Shell", "recycled": 55.0, "recyc_cls": "Automotive Dismantling Steel Recovery (Class A)",
            "raw": "Tesla 4680 Dry-Electrode Battery Cells, High-Voltage 800V Busbars, SiC Power Stage", "origin": "USA (Austin/Kearny) / South Korea",
            "proc": "Air-Bending Stainless Stamping & Continuous 4680 Dry Battery Assembly", "tier1": "Tesla Gigafactory Texas (Austin, TX)", "tier1_reg": "North America",
            "tier2": "Outokumpu / Aperam Specialty Stainless Steel Mills", "tier2_reg": "Europe / North America",
            "tier3": "BHP Nickel West & Piedmont Lithium", "tier3_reg": "Australia / North America",
            "choke": "Strait of Hormuz", "lane": "Global Primary Nickel / Stainless Supply Corridors", "delay": 18,
            "vuln": "Section 232 stainless steel tariffs & dry-electrode battery ramp-up bottlenecks",
            "retail": 79990.00, "wholesale": 56000.00, "pkg_base": 24500.00, "raw_base": 16800.00, "freight_base": 1850.00,
            "carbon": 12800.0, "ppwr": "Compliant (Recyclable Stainless Steel)", "tariff": True
        },
        {
            "brand": "Tesla", "parent": "Tesla, Inc.", "subcat": "Mid-Size Electric Crossover SUV",
            "name": "Tesla Model Y Long Range AWD (Structural LFP/NMC Pack)", "archetype": "EV SKATEBOARD CHASSIS",
            "mass": 510000.0, "mat": "Single-Piece Cast Aluminum Front & Rear Bodies",
            "closure": "Gigacasted Shock Towers with High-Strength Aluminum Crush Tubes", "closure_mass": 138000.0,
            "barrier": "Structural Adhesive Battery Pack Seal (IP67 Immersion Protection)", "recycled": 40.0, "recyc_cls": "High-Efficiency Battery Cell Recovery (Class A)",
            "raw": "High-Density Cylindrical/Prismatic Cells, 48V Low-Voltage Harness, SiC Inverters", "origin": "USA / Germany / China",
            "proc": "Integrated Robotic Structural Body Welded Line", "tier1": "Tesla Gigafactory Berlin-Brandenburg (Grünheide, Germany)", "tier1_reg": "Central Europe",
            "tier2": "CATL / LG Energy Solution (Erfurt / Wrocław)", "tier2_reg": "Central Europe",
            "tier3": "European Recycled Aluminum Ingot & Lithium Carbonate", "tier3_reg": "Western Europe",
            "choke": "Bab el-Mandeb / Red Sea", "lane": "Asian Cell Component Supply to European Giga Fabs via Suez", "delay": 14,
            "vuln": "Red Sea detour delays critical cell electrolyte arrivals by 14 days, inflating European assembly costs",
            "retail": 47990.00, "wholesale": 32200.00, "pkg_base": 13800.00, "raw_base": 9600.00, "freight_base": 1100.00,
            "carbon": 8900.0, "ppwr": "Compliant (EU Battery Passport 2026)", "tariff": False
        },
        {
            "brand": "BYD", "parent": "BYD Company Limited", "subcat": "Aerodynamic Electric Sedan",
            "name": "BYD Seal Excellence AWD (82.5kWh Blade Battery CTB)", "archetype": "BLADE BATTERY UNIBODY",
            "mass": 490000.0, "mat": "Cell-to-Body (CTB) Integrated Honeycomb Aluminum Floor Structure",
            "closure": "Extruded Aluminum Side Sills + Direct-Bonded Top Cover", "closure_mass": 98000.0,
            "barrier": "Ceramic Thermal Insulation Layer (Nail Penetration Tested)", "recycled": 35.0, "recyc_cls": "Lithium Iron Phosphate Pyrometallurgical Recovery (Class B)",
            "raw": "BYD FinDreams Lithium Iron Phosphate (LFP) Blade Cells, 8-in-1 Electric Powertrain", "origin": "China (Shenzhen/Xi'an)",
            "proc": "Continuous Automated Cell-to-Body Packless Assembly", "tier1": "BYD Auto Production Hub (Changzhou, China)", "tier1_reg": "East Asia",
            "tier2": "FinDreams Battery Mega-Hub (Bishan, Chongqing)", "tier2_reg": "East Asia",
            "tier3": "Sichuan Lithium Salt Lake Refineries & Iron Phosphate Plants", "tier3_reg": "East Asia",
            "choke": "Malacca Strait", "lane": "Shenzhen to European & Southeast Asian Automotive RORO Terminals", "delay": 16,
            "vuln": "EU Anti-Subsidy Tariff Investigations (+38.1%) & Malacca Strait shipping congestion",
            "retail": 44990.00, "wholesale": 26800.00, "pkg_base": 9800.00, "raw_base": 8400.00, "freight_base": 1650.00,
            "carbon": 7400.0, "ppwr": "Transition Risk (EU Subsidies / Tariffs)", "tariff": True
        },
        {
            "brand": "Porsche", "parent": "Dr. Ing. h.c. F. Porsche AG (Volkswagen Group)", "subcat": "Luxury Performance Electric Sports Car",
            "name": "Porsche Taycan Turbo S (97kWh Performance Battery Plus)", "archetype": "EXTRUDED ALU MONOCOQUE",
            "mass": 560000.0, "mat": "Multi-Material Aluminum-Steel Hybrid Spaceframe Monocoque",
            "closure": "Bolted Underbody Crash Shield with Integrated Cooling Channels", "closure_mass": 185000.0,
            "barrier": "800-Volt Carbon-Fiber Reinforced Polymer (CFRP) Thermal Shield", "recycled": 48.0, "recyc_cls": "OEM Closed-Loop Dismantling & Remanufacturing (Class A)",
            "raw": "High-Nickel 800V Pouch Cells, Permanently Excited Dual Motors, Two-Speed Transmission", "origin": "Germany / Poland / Sweden",
            "proc": "Cold Metal Transfer (CMT) Welding & Flexible Assembly (Zuffenhausen)", "tier1": "Dr. Ing. h.c. F. Porsche AG (Stuttgart-Zuffenhausen)", "tier1_reg": "Central Europe",
            "tier2": "Dräxlmaier Battery System Factory (Sachsenheim, Germany)", "tier2_reg": "Central Europe",
            "tier3": "Northvolt Sustainable Cathode Materials & European Hydro Nickel", "tier3_reg": "Northern Europe",
            "choke": "Strait of Hormuz", "lane": "European High-Grade Aluminum Smelting & Global Export Lanes", "delay": 12,
            "vuln": "German energy price volatility for aluminum melting & Gulf primary metal delivery premiums",
            "retail": 174900.00, "wholesale": 112000.00, "pkg_base": 38000.00, "raw_base": 34000.00, "freight_base": 3200.00,
            "carbon": 14200.0, "ppwr": "Compliant (EU Battery Passport 2026)", "tariff": False
        }
    ]

    while len(all_records) < 6000:
        tpl = random.choice(ev_templates)
        jitter = round(random.uniform(0.96, 1.10), 2)
        retail_p = round(tpl["retail"] * jitter, 2)
        wholesale_p = round(tpl["wholesale"] * jitter, 2)
        pkg_base = round(tpl["pkg_base"] * jitter, 2)
        raw_base = round(tpl["raw_base"] * jitter, 2)
        freight_base = round(tpl["freight_base"] * jitter, 2)

        shock_mult = random.uniform(1.28, 1.52)
        pkg_shock = round(pkg_base * shock_mult, 2)
        freight_shock = round(freight_base * 2.2, 2)
        unmitigated_retail = round(retail_p + (pkg_shock - pkg_base) * 1.35 + (freight_shock - freight_base), 2)
        defended_retail = round(retail_p + (pkg_shock - pkg_base) * 0.20, 2)
        savings = round(unmitigated_retail - defended_retail, 2)

        vin = f"5YJ3E1EB{item_id:09d}"[:17]

        all_records.append({
            "sector": "Electric Vehicles & Automotive",
            "sku_id": f"SKU-{item_id}",
            "gtin_barcode": vin,
            "product_name": tpl["name"],
            "brand": tpl["brand"],
            "parent_company": tpl["parent"],
            "category": "Electric Vehicles",
            "subcategory": tpl["subcat"],
            "net_weight_volume": f"{tpl['mass']/1000.0:.0f}kg",
            "shelf_life_days": 3650,
            "container_archetype": tpl["archetype"],
            "primary_container_material": tpl["mat"],
            "packaging_mass_grams": tpl["mass"],
            "closure_type": tpl["closure"],
            "closure_mass_grams": tpl["closure_mass"],
            "seal_liner_barrier": tpl["barrier"],
            "recycled_content_pct": tpl["recycled"],
            "recyclability_class": tpl["recyc_cls"],
            "primary_raw_materials": tpl["raw"],
            "raw_material_origin_country": tpl["origin"],
            "processing_technology": tpl["proc"],
            "tier1_converter": tpl["tier1"],
            "tier1_converter_region": tpl["tier1_reg"],
            "tier2_processor_region": tpl["tier2_reg"],
            "tier3_origin_region": tpl["tier3_reg"],
            "critical_chokepoints": tpl["choke"],
            "shipping_lane_exposure": tpl["lane"],
            "cape_detour_transit_delay_days": tpl["delay"],
            "primary_chokepoint_vulnerability": tpl["vuln"],
            "wholesale_price_usd": wholesale_p,
            "retail_price_usd": retail_p,
            "packaging_baseline_cost_usd": pkg_base,
            "raw_content_cost_usd": raw_base,
            "freight_baseline_usd": freight_base,
            "unmitigated_shock_packaging_cost_usd": pkg_shock,
            "unmitigated_retail_shelf_price_usd": unmitigated_retail,
            "basketshield_defended_shelf_price_usd": defended_retail,
            "consumer_savings_per_unit_usd": savings,
            "gross_margin_pct": round(((retail_p - wholesale_p) / retail_p) * 100.0, 1),
            "scope3_packaging_carbon_kg_co2e": tpl["carbon"],
            "eu_ppwr_status": tpl["ppwr"],
            "section_232_tariff_applies": tpl["tariff"]
        })
        item_id += 1

    df = pd.DataFrame(all_records[:6000])
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {len(df)} comprehensive multi-sector items in: {output_path}")
    return df

if __name__ == "__main__":
    generate_grocery_catalog()
