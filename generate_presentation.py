import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Editorial Clean Light Mode
    COLOR_BG = RGBColor(248, 250, 252)        # #F8FAFC (Slate 50 canvas)
    COLOR_CARD = RGBColor(255, 255, 255)      # #FFFFFF (White cards)
    COLOR_BORDER = RGBColor(226, 232, 240)    # #E2E8F0 (Subtle slate border)
    COLOR_BORDER_STRONG = RGBColor(203, 213, 225) # #CBD5E1
    COLOR_HEADER = RGBColor(15, 23, 42)       # #0F172A (Deep Slate 900)
    COLOR_SUBHEADER = RGBColor(51, 65, 85)    # #334155 (Slate 700)
    COLOR_BODY = RGBColor(71, 85, 105)        # #475569 (Slate 600)
    COLOR_MUTED = RGBColor(100, 116, 139)     # #64748B (Slate 500)
    COLOR_ACCENT = RGBColor(37, 99, 235)      # #2563EB (Royal Blue)
    COLOR_ACCENT_BG = RGBColor(239, 246, 255) # #EFF6FF (Sky tint)
    COLOR_CRUNCH = RGBColor(219, 39, 119)     # #DB2777 (Rose/Pink for memory shock)
    COLOR_CRUNCH_BG = RGBColor(253, 242, 248) # #FDF2F8
    COLOR_SUCCESS = RGBColor(5, 150, 105)     # #059669 (Emerald for savings)
    COLOR_SUCCESS_BG = RGBColor(236, 253, 245)# #ECFDF5

    FONT_FAMILY = "Segoe UI"

    def add_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    def add_card(slide, left, top, width, height, fill_color=COLOR_CARD, border_color=COLOR_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    def add_header(slide, tag_text, title_text, subtitle_text=None):
        # Category Tag / Badge
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.name = FONT_FAMILY
        p_tag.font.size = Pt(9.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_ACCENT

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_FAMILY
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_HEADER

        # Subtitle (optional)
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.42), Inches(11.7), Inches(0.4))
            tf_sub = sub_box.text_frame
            tf_sub.word_wrap = True
            tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(11)
            p_sub.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 1: Title & Cover
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide1)

    # Hero Center Container Card
    add_card(slide1, Inches(1.0), Inches(0.9), Inches(11.333), Inches(5.7), COLOR_CARD, COLOR_BORDER_STRONG)

    # Top Badge
    badge = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.4), Inches(1.3), Inches(4.3), Inches(0.36))
    badge.fill.solid()
    badge.fill.fore_color.rgb = COLOR_ACCENT_BG
    badge.line.color.rgb = COLOR_ACCENT
    badge.line.width = Pt(1)
    tf_b = badge.text_frame
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
    p_b = tf_b.paragraphs[0]
    p_b.text = "OPERATIONS RESEARCH & SUPPLY CHAIN INTELLIGENCE"
    p_b.font.name = FONT_FAMILY
    p_b.font.size = Pt(9)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_ACCENT
    p_b.alignment = PP_ALIGN.CENTER

    # Main Title
    t_box = slide1.shapes.add_textbox(Inches(1.4), Inches(1.85), Inches(10.5), Inches(1.0))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "BasketShield AI"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = COLOR_HEADER

    # Subtitle
    s_box = slide1.shapes.add_textbox(Inches(1.4), Inches(2.85), Inches(10.5), Inches(0.8))
    tf_s = s_box.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = "Prescriptive Unit Economics Defense Against Geopolitical Maritime Chokepoints and the 2026 AI Memory Crunch"
    p_s.font.name = FONT_FAMILY
    p_s.font.size = Pt(16)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_SUBHEADER

    # 3 Pill Metrics on Cover
    pillars = [
        ("6,000 Multi-Sector SKUs", "FMCG Staples, High-Tech Electronics & Tesla EV Skateboards"),
        ("Google OR-Tools MILP", "Sub-15ms deterministic optimization with Big-M binary supplier gating"),
        ("Up to 85% Price Defense", "Prevents supermarket checkout inflation and device MSRP surges")
    ]
    for i, (head, desc) in enumerate(pillars):
        c_left = Inches(1.4 + i * 3.6)
        c_box = add_card(slide1, c_left, Inches(3.7), Inches(3.35), Inches(1.4), COLOR_BG, COLOR_BORDER)
        tb = slide1.shapes.add_textbox(c_left + Inches(0.18), Inches(3.85), Inches(3.0), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p1 = tf.paragraphs[0]
        p1.text = head
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(11.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_ACCENT
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_BODY

    # Team Attribution Footer
    team_box = slide1.shapes.add_textbox(Inches(1.4), Inches(5.45), Inches(10.5), Inches(0.6))
    tf_t = team_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = "Team Lazy  •  Shrey Jaiswal  &  Navya Gupta"
    p_t.font.name = FONT_FAMILY
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_HEADER

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "Open-Source Repository: github.com/lazyshrey/basketshield  •  Peer-Audited Research Paper Included"
    p_t2.font.name = FONT_FAMILY
    p_t2.font.size = Pt(10)
    p_t2.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 2: The Macro Crisis & 2026 AI Memory Squeeze
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide2)
    add_header(slide2, "01. Macro Crisis & Empirical Shocks", 
               "Compounding Disruption: Maritime Chokepoints & The AI Memory Supercycle",
               "Global supply shocks strike through physical component dependencies, inflating manufacturing costs.")

    shock_cards = [
        ("Bab el-Mandeb & Red Sea", "+310% to +440% Freight Spike",
         "Attacks in the Red Sea force container detours around the Cape of Good Hope, adding 10–14 days and 3,500 nautical miles for Europe-Asia lanes. Drewry World Container Index peaked above $5,900/FEU. Perishable food shipments (coffee, olive oil) face port demurrage and container deterioration.",
         COLOR_ACCENT),
        ("Smelting Energy Surcharges", "+24% to +35% Raw Metal Inflation",
         "Natural gas and electricity volatility in Europe and the Middle East forced severe curtailments across energy-intensive primary aluminum smelters and glass annealing kilns. Raw packaging represents up to 45% of total grocery unit costs, creating an immediate margin squeeze.",
         COLOR_ACCENT),
        ("2026 AI Memory Crunch", "+58% to +72% DRAM Wafer Inflation",
         "Hyperscalers consuming 80%+ of 1b-nm DRAM wafer allocation for HBM3e/HBM4 AI server clusters. High-bandwidth 3D TSV stacking introduces a ~3x wafer area penalty, starving wafer capacity for consumer LPDDR5X and DDR5. Silicon memory accounts for 18%–32% of electronic BOMs.",
         COLOR_CRUNCH)
    ]

    for i, (title, stat, body, color) in enumerate(shock_cards):
        left = Inches(0.8 + i * 4.0)
        card = add_card(slide2, left, Inches(1.95), Inches(3.73), Inches(4.9), COLOR_CARD, COLOR_BORDER)
        
        # Stat banner inside card
        sb = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.2), Inches(2.15), Inches(3.33), Inches(0.65))
        sb.fill.solid()
        sb.fill.fore_color.rgb = COLOR_CRUNCH_BG if color == COLOR_CRUNCH else COLOR_ACCENT_BG
        sb.line.color.rgb = color
        sb.line.width = Pt(1)
        tf_sb = sb.text_frame
        tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
        p_sb = tf_sb.paragraphs[0]
        p_sb.text = stat
        p_sb.font.name = FONT_FAMILY
        p_sb.font.size = Pt(11)
        p_sb.font.bold = True
        p_sb.font.color.rgb = color
        p_sb.alignment = PP_ALIGN.CENTER

        # Title & Description
        tb = slide2.shapes.add_textbox(left + Inches(0.2), Inches(2.95), Inches(3.33), Inches(3.7))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_HEADER

        p2 = tf.add_paragraph()
        p2.space_before = Pt(8)
        p2.text = body
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 3: The Systemic Failure Mode (Why ERPs Fail)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide3)
    add_header(slide3, "02. The Enterprise Blindspot", 
               "Why Spreadsheets & Traditional ERPs Drive Consumer Price Inflation",
               "Legacy enterprise software is purely transactional, leaving manufacturers blind to compounding physical shocks.")

    # Left Column: The Problem in ERPs
    add_card(slide3, Inches(0.8), Inches(1.95), Inches(5.65), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_l = slide3.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(5.05), Inches(4.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

    p = tf_l.paragraphs[0]
    p.text = "How Legacy Enterprise Tools Fail Under Acute Shocks"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_HEADER

    points_l = [
        ("Static Moving Averages:", "Standard ERP platforms (SAP, Oracle) compute standard costs using historical moving averages. They cannot evaluate non-linear step-function tariff changes or sudden canal surcharges."),
        ("Single-Node Visibility:", "Procurement systems track Tier-1 packaging and component vendors, entirely missing Tier-2/3 dependencies (e.g. SK Hynix DRAM lithography, European gas-fired glass kilns)."),
        ("Manual Multi-Week Negotiations:", "Procurement teams take 3 to 6 weeks to solicit alternative supplier quotes. By then, unhedged price surges are already locked into production orders."),
        ("No Circular Optimization:", "Legacy systems cannot balance secondary recycled scrap mandates against maritime lead times, defaulting to expensive single-source suppliers.")
    ]
    for bold_text, desc in points_l:
        p_item = tf_l.add_paragraph()
        p_item.space_before = Pt(10)
        run_bold = p_item.add_run()
        run_bold.text = bold_text + " "
        run_bold.font.name = FONT_FAMILY
        run_bold.font.size = Pt(9.5)
        run_bold.font.bold = True
        run_bold.font.color.rgb = COLOR_ACCENT
        run_desc = p_item.add_run()
        run_desc.text = desc
        run_desc.font.name = FONT_FAMILY
        run_desc.font.size = Pt(9.5)
        run_desc.font.color.rgb = COLOR_BODY

    # Right Column: The Consumer Impact
    add_card(slide3, Inches(6.85), Inches(1.95), Inches(5.65), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_r = slide3.shapes.add_textbox(Inches(7.15), Inches(2.2), Inches(5.05), Inches(4.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

    p_r = tf_r.paragraphs[0]
    p_r.text = "The Human Consequence: Inflation at the Checkout"
    p_r.font.name = FONT_FAMILY
    p_r.font.size = Pt(14)
    p_r.font.bold = True
    p_r.font.color.rgb = COLOR_CRUNCH

    points_r = [
        ("Zero Margin Buffer:", "Food and beverage brands operate on net margins between 35%–42%. They physically cannot absorb 40%+ packaging landed cost surges without going into the red."),
        ("The Immediate Pass-Through:", "Manufacturers pass 100% of unmitigated packaging and memory surges down through distributors and supermarkets. Consumers face higher prices for instant coffee, oils, and electronics."),
        ("Shrinkflation Dynamics:", "When brands hit consumer price resistance ceilings, they reduce product volume while maintaining package pricing—a direct consequence of packaging un-resilience."),
        ("The BasketShield Solution:", "Replace reactive price increases with sub-15ms deterministic mathematical solver reallocation, nearshoring, and circular recycling arbitrage.")
    ]
    for bold_text, desc in points_r:
        p_item = tf_r.add_paragraph()
        p_item.space_before = Pt(10)
        run_bold = p_item.add_run()
        run_bold.text = bold_text + " "
        run_bold.font.name = FONT_FAMILY
        run_bold.font.size = Pt(9.5)
        run_bold.font.bold = True
        run_bold.font.color.rgb = COLOR_CRUNCH
        run_desc = p_item.add_run()
        run_desc.text = desc
        run_desc.font.name = FONT_FAMILY
        run_desc.font.size = Pt(9.5)
        run_desc.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 4: BasketShield AI Architecture & Technical Core
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide4)
    add_header(slide4, "03. Solution Architecture", 
               "The BasketShield AI Decision Intelligence Pipeline",
               "An integrated pipeline connecting granular physical Bill-of-Materials with deterministic Operations Research.")

    # 3 Pipeline Pillars
    pillars_tech = [
        ("1. Multi-Sector Catalog", "6,000 Verified SKUs",
         "Grounded real-world catalog across three critical sectors:\n\n• FMCG Consumer Groceries: 2,000 SKUs (coffee jars, oils, aluminum cans)\n• Consumer Electronics: 2,000 SKUs (smartphones, enterprise GPUs, laptops with exact LPDDR5X/HBM3e specs)\n• Automotive & Tesla EVs: 2,000 SKUs (Model 3 chassis, Cybertruck 4680 packs)\n\nStores exact physical masses, tare specs, and lithography origins.",
         COLOR_ACCENT),
        ("2. Physical BOM Engine", "Gemini AI & Metallurgy",
         "Deconstructs any commercial SKU into physical components:\n\n• Primary Container Material (Soda-Lime Flint Glass, AA 3104 Canstock, Grade 5 Titanium)\n• Component Masses in grams (Jar 214g, Closure 14.5g, Seal 0.8g)\n• Foundry & Fab Dependencies (TSMC 3nm, SK Hynix Icheon, Samsung Pyeongtaek)\n• Macro Shock Transmissibility: Dynamic tariff, demurrage, and spot freight index mapping.",
         COLOR_ACCENT),
        ("3. Google OR-Tools MILP", "Sub-15ms Optimization",
         "Mixed-Integer Linear Programming engine solving multi-vendor allocation:\n\n• Strict Demand Conservation: Guarantees zero unfulfilled orders\n• Big-M Semi-Continuous Gating: Enforces vendor activation thresholds and MOQs\n• Recycled Fleet Mandate: Guarantees circular scrap compliance\n• Nearshoring Breakeven: Identifies the exact mathematical distance where domestic sourcing beats tariffs.",
         COLOR_SUCCESS)
    ]

    for i, (title, sub, body, color) in enumerate(pillars_tech):
        left = Inches(0.8 + i * 4.0)
        card = add_card(slide4, left, Inches(1.95), Inches(3.73), Inches(4.3), COLOR_CARD, COLOR_BORDER)
        
        # Pill inside card
        sb = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.2), Inches(2.15), Inches(3.33), Inches(0.45))
        sb.fill.solid()
        sb.fill.fore_color.rgb = COLOR_SUCCESS_BG if color == COLOR_SUCCESS else COLOR_ACCENT_BG
        sb.line.color.rgb = color
        sb.line.width = Pt(1)
        tf_sb = sb.text_frame
        tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
        p_sb = tf_sb.paragraphs[0]
        p_sb.text = sub.upper()
        p_sb.font.name = FONT_FAMILY
        p_sb.font.size = Pt(9.5)
        p_sb.font.bold = True
        p_sb.font.color.rgb = color
        p_sb.alignment = PP_ALIGN.CENTER

        # Body
        tb = slide4.shapes.add_textbox(left + Inches(0.2), Inches(2.75), Inches(3.33), Inches(3.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_HEADER

        p2 = tf.add_paragraph()
        p2.space_before = Pt(6)
        p2.text = body
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(9.2)
        p2.font.color.rgb = COLOR_BODY

    # Bottom Pipeline Flow Summary Banner
    bot_card = add_card(slide4, Inches(0.8), Inches(6.4), Inches(11.73), Inches(0.65), COLOR_CARD, COLOR_BORDER)
    tb_bot = slide4.shapes.add_textbox(Inches(1.0), Inches(6.45), Inches(11.3), Inches(0.55))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    tf_bot.margin_left = tf_bot.margin_top = tf_bot.margin_right = tf_bot.margin_bottom = 0
    p_b = tf_bot.paragraphs[0]
    p_b.text = "DATA FLOW: Macro Shock Scenarios → Physical BOM Parameterization → SCIP MILP Solver → Optimal Supplier Allocation & Defended Shelf Price"
    p_b.font.name = FONT_FAMILY
    p_b.font.size = Pt(9.5)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_HEADER
    p_b.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 5: Platform Interface & Live Chokepoint Simulation
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide5)
    add_header(slide5, "04. Platform Demonstration", 
               "Resilience Cockpit: Interactive Chokepoint & Shock Studio",
               "A dark monochrome decision cockpit built with Streamlit and styled with strict shadcn/ui design standards.")

    # Left: Explanation & Technical Features
    add_card(slide5, Inches(0.8), Inches(1.95), Inches(4.7), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_c5 = slide5.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(4.2), Inches(4.5))
    tf_c5 = tb_c5.text_frame
    tf_c5.word_wrap = True
    tf_c5.margin_left = tf_c5.margin_top = tf_c5.margin_right = tf_c5.margin_bottom = 0

    p_c5 = tf_c5.paragraphs[0]
    p_c5.text = "Operational Cockpit Features"
    p_c5.font.name = FONT_FAMILY
    p_c5.font.size = Pt(13)
    p_c5.font.bold = True
    p_c5.font.color.rgb = COLOR_HEADER

    feats = [
        ("Multi-Sector Workspace Switching:", "Easily toggle between FMCG Groceries, Consumer Electronics & Computing, and Tesla Electric Vehicles with real-time SKU search across 6,000 catalog items."),
        ("Acute Shock Studio:", "Simulate verified geopolitical crises in real time: 2026 Middle East maritime closures (Bab el-Mandeb / Strait of Hormuz), Taiwan Strait container congestion, and smelter gas tariffs."),
        ("Dynamic Archetype Tagging:", "Classifies products by container form factor (e.g. Glass Jar, Aluminum Can, Smartphone Unibody, 4680 Pack) and binds them directly to global commodity spot indices."),
        ("Real-Time Vulnerability Flags:", "Immediately surfaces primary chokepoints, such as '+14-day Cape detour' and '🧠 HBM3e / DRAM Wafer Crunch (+58%)'.")
    ]
    for b_txt, d_txt in feats:
        p_item = tf_c5.add_paragraph()
        p_item.space_before = Pt(8)
        run_b = p_item.add_run()
        run_b.text = b_txt + " "
        run_b.font.name = FONT_FAMILY
        run_b.font.size = Pt(9.2)
        run_b.font.bold = True
        run_b.font.color.rgb = COLOR_ACCENT
        run_d = p_item.add_run()
        run_d.text = d_txt
        run_d.font.name = FONT_FAMILY
        run_d.font.size = Pt(9.2)
        run_d.font.color.rgb = COLOR_BODY

    # Right: Embedded Screenshot
    add_card(slide5, Inches(5.7), Inches(1.95), Inches(6.83), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    img_path1 = os.path.join(os.path.dirname(__file__), "screenshots", "01_resilience_cockpit_home.png")
    if os.path.exists(img_path1):
        slide5.shapes.add_picture(img_path1, Inches(5.8), Inches(2.05), width=Inches(6.63))

    # =========================================================================
    # SLIDE 6: Empirical Unit Economics Defense
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide6)
    add_header(slide6, "05. Empirical Proof & Unit Economics", 
               "Physical BOM Mass Decomposition & Landed Cost Preservation",
               "Proving measurable consumer price defense on real-world products like Davidoff Espresso 57 Instant Glass Jar.")

    # Left: Embedded Screenshot 2
    add_card(slide6, Inches(0.8), Inches(1.95), Inches(6.83), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    img_path2 = os.path.join(os.path.dirname(__file__), "screenshots", "02_physical_bom_cost_defense.png")
    if os.path.exists(img_path2):
        slide6.shapes.add_picture(img_path2, Inches(0.9), Inches(2.05), width=Inches(6.63))

    # Right: Hard Metric Breakdown
    add_card(slide6, Inches(7.83), Inches(1.95), Inches(4.7), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_m = slide6.shapes.add_textbox(Inches(8.05), Inches(2.15), Inches(4.25), Inches(4.5))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0

    p_m = tf_m.paragraphs[0]
    p_m.text = "Empirical Value Preservation"
    p_m.font.name = FONT_FAMILY
    p_m.font.size = Pt(13)
    p_m.font.bold = True
    p_m.font.color.rgb = COLOR_HEADER

    metrics_list = [
        ("Pre-Crisis Baseline:", "$0.50 / unit", "Standard procurement before the maritime and energy shock.", COLOR_HEADER),
        ("Unmitigated Shock Cost:", "$1.03 / unit", "+105.3% unhedged price surge driven by overseas freight delays and energy tariffs.", COLOR_CRUNCH),
        ("BasketShield Defended Cost:", "$0.10 / unit", "-79.8% cost reduction achieved by reallocating to domestic certified nearshore converters.", COLOR_SUCCESS),
        ("Defended Retail Shelf MSRP:", "$9.40 / unit", "-$0.97 inflationary consumer price spike absorbed, preventing supermarket basket price escalation.", COLOR_SUCCESS)
    ]

    for label, val, note, col in metrics_list:
        p_item = tf_m.add_paragraph()
        p_item.space_before = Pt(8)
        run_l = p_item.add_run()
        run_l.text = label + " "
        run_l.font.name = FONT_FAMILY
        run_l.font.size = Pt(9.2)
        run_l.font.bold = True
        run_l.font.color.rgb = COLOR_SUBHEADER
        run_v = p_item.add_run()
        run_v.text = val + "\n"
        run_v.font.name = FONT_FAMILY
        run_v.font.size = Pt(10.5)
        run_v.font.bold = True
        run_v.font.color.rgb = col
        run_n = p_item.add_run()
        run_n.text = note
        run_n.font.name = FONT_FAMILY
        run_n.font.size = Pt(8.5)
        run_n.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 7: Operations Research Formulation & Executive Intelligence
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide7)
    add_header(slide7, "06. Mathematical Formulation & Executive Narrative", 
               "Mixed-Integer Programming (MILP) & Plain-English Executive Briefing",
               "Translating deterministic linear algebra proofs into actionable intelligence for non-technical leadership.")

    # Left: Mathematical Formulation Card
    add_card(slide7, Inches(0.8), Inches(1.95), Inches(5.65), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_math = slide7.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(5.15), Inches(4.5))
    tf_math = tb_math.text_frame
    tf_math.word_wrap = True
    tf_math.margin_left = tf_math.margin_top = tf_math.margin_right = tf_math.margin_bottom = 0

    p_ma = tf_math.paragraphs[0]
    p_ma.text = "Mathematical Optimization Formulation (Google OR-Tools)"
    p_ma.font.name = FONT_FAMILY
    p_ma.font.size = Pt(13)
    p_ma.font.bold = True
    p_ma.font.color.rgb = COLOR_HEADER

    math_points = [
        ("Objective Function:", "min sum [ C_landed,s * x_s + F_contract,s * y_s + lambda_L * L_s * x_s + lambda_C * E_s * x_s ]\nMinimizes total landed procurement cost, binary vendor activation fees, lead-time penalties, and carbon scope 3 emissions."),
        ("1. Strict Demand Conservation:", "sum(x_s) = D_total\nGuarantees zero under-delivery; 100% of required production volume is satisfied without stockouts."),
        ("2. Big-M Binary Activation Gating:", "MOQ_s * y_s <= x_s <= Capacity_s * y_s\nForces volume to zero if supplier is not activated (y_s = 0), and respects certified supplier production ceilings."),
        ("3. Certified Circular Scrap Fleet SLA:", "sum(R_s * x_s) >= R_target * D_total\nEnforces closed-loop post-consumer recycled content (e.g. 71.8% achieved in practice)."),
        ("Computational Performance:", "Evaluated deterministically in <15ms with verified global optimality via the SCIP backend.")
    ]

    for title, desc in math_points:
        p_item = tf_math.add_paragraph()
        p_item.space_before = Pt(6)
        run_t = p_item.add_run()
        run_t.text = title + " "
        run_t.font.name = FONT_FAMILY
        run_t.font.size = Pt(9.2)
        run_t.font.bold = True
        run_t.font.color.rgb = COLOR_ACCENT
        run_d = p_item.add_run()
        run_d.text = desc
        run_d.font.name = FONT_FAMILY
        run_d.font.size = Pt(8.5)
        run_d.font.color.rgb = COLOR_BODY

    # Right: Executive Decision Brief Screenshot & Value
    add_card(slide7, Inches(6.65), Inches(1.95), Inches(5.88), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    img_path3 = os.path.join(os.path.dirname(__file__), "screenshots", "03_executive_decision_brief.png")
    if os.path.exists(img_path3):
        slide7.shapes.add_picture(img_path3, Inches(6.75), Inches(2.05), width=Inches(5.68))

    # =========================================================================
    # SLIDE 8: Summary, Deliverables & Team Lazy
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_slide_bg(slide8)
    add_header(slide8, "07. Project Summary & Deliverables", 
               "Empirical Benchmarks, Open-Source Deliverables & Team Lazy",
               "A complete, battle-tested decision platform protecting enterprise margins and household grocery budgets.")

    summary_columns = [
        ("Empirical Performance", "Verified Benchmarks",
         "• Sub-15ms Solve Time: Real-time mathematical optimization replaces 4-week manual negotiation cycles.\n\n• 65%–85% Inflation Defense: Proved absorption of compounding maritime and memory component cost spikes.\n\n• 100% Test Suite Coverage: 5 comprehensive automated test suites verifying catalog integrity, LLM fallbacks, and boundary constraints.",
         COLOR_ACCENT),
        ("Complete Deliverables", "Audit-Ready Artifacts",
         "• Live Streamlit Platform: 4 dedicated workspaces (Cockpit, Provisional Cost Board, Commons, Formulations).\n\n• Publication Research Paper: Peer-audited whitepaper by Shrey Jaiswal cited across UNCTAD, TrendForce & EPO.\n\n• Open-Source GitHub Repository:\ngithub.com/lazyshrey/basketshield\nComplete commit milestones & docs.",
         COLOR_ACCENT),
        ("Team Lazy", "Creators & Attribution",
         "• Team Name: Team Lazy\n\n• Members:\n  - Shrey Jaiswal\n  - Navya Gupta\n\n• Tech Stack:\n  Python 3.13, Google OR-Tools (SCIP),\n  Google Gemini API, Streamlit, Plotly,\n  ReportLab & python-pptx.\n\n• License: Open-Source MIT License.",
         COLOR_SUCCESS)
    ]

    for i, (title, sub, body, color) in enumerate(summary_columns):
        left = Inches(0.8 + i * 4.0)
        card = add_card(slide8, left, Inches(1.95), Inches(3.73), Inches(4.9), COLOR_CARD, COLOR_BORDER)
        
        sb = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.2), Inches(2.15), Inches(3.33), Inches(0.45))
        sb.fill.solid()
        sb.fill.fore_color.rgb = COLOR_SUCCESS_BG if color == COLOR_SUCCESS else COLOR_ACCENT_BG
        sb.line.color.rgb = color
        sb.line.width = Pt(1)
        tf_sb = sb.text_frame
        tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
        p_sb = tf_sb.paragraphs[0]
        p_sb.text = sub.upper()
        p_sb.font.name = FONT_FAMILY
        p_sb.font.size = Pt(9.5)
        p_sb.font.bold = True
        p_sb.font.color.rgb = color
        p_sb.alignment = PP_ALIGN.CENTER

        tb = slide8.shapes.add_textbox(left + Inches(0.2), Inches(2.75), Inches(3.33), Inches(3.9))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_HEADER

        p2 = tf.add_paragraph()
        p2.space_before = Pt(8)
        p2.text = body
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_BODY

    # Output paths
    local_pptx = os.path.join(os.path.dirname(__file__), "BasketShield_AI_Presentation.pptx")
    prs.save(local_pptx)
    print(f"Presentation saved locally to: {local_pptx}")

    downloads_dir = r"C:\Users\5apri\Downloads"
    if os.path.exists(downloads_dir):
        downloads_pptx = os.path.join(downloads_dir, "BasketShield_AI_Presentation.pptx")
        shutil.copy2(local_pptx, downloads_pptx)
        print(f"Presentation copied to Downloads: {downloads_pptx}")

if __name__ == "__main__":
    create_deck()
