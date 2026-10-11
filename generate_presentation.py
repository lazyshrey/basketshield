import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Clean Hackathon Editorial Color Palette
    COLOR_BG = RGBColor(248, 250, 252)          # #F8FAFC (Clean soft canvas)
    COLOR_CARD = RGBColor(255, 255, 255)        # #FFFFFF (White cards)
    COLOR_BORDER = RGBColor(226, 232, 240)      # #E2E8F0 (Subtle border)
    COLOR_BORDER_STRONG = RGBColor(203, 213, 225) # #CBD5E1
    COLOR_HEADER = RGBColor(15, 23, 42)         # #0F172A (Deep Slate 900)
    COLOR_SUBHEADER = RGBColor(51, 65, 85)      # #334155 (Slate 700)
    COLOR_BODY = RGBColor(71, 85, 105)          # #475569 (Slate 600)
    COLOR_MUTED = RGBColor(100, 116, 139)       # #64748B (Slate 500)
    
    # Accent Colors
    COLOR_BLUE = RGBColor(37, 99, 235)          # #2563EB (Brand Blue)
    COLOR_BLUE_BG = RGBColor(239, 246, 255)     # #EFF6FF (Soft Blue)
    COLOR_RED = RGBColor(225, 29, 72)           # #E11D48 (Crisis / Shock Red)
    COLOR_RED_BG = RGBColor(255, 241, 242)      # #FFF1F2 (Soft Red)
    COLOR_GREEN = RGBColor(13, 148, 136)        # #0D9488 (Savings / Defended Teal)
    COLOR_GREEN_BG = RGBColor(240, 253, 250)    # #F0FDFA (Soft Green)

    FONT_FAMILY = "Segoe UI"

    # Helper: Slide background
    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    # Helper: Card with subtle border
    def add_card(slide, left, top, width, height, fill_color=COLOR_CARD, border_color=COLOR_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # Helper: Clean header (Tag + Big Title + Subtitle)
    def add_header(slide, tag_text, title_text, subtitle_text):
        # Tag Badge
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.42), Inches(3.2), Inches(0.32))
        tag.fill.solid()
        tag.fill.fore_color.rgb = COLOR_BLUE_BG
        tag.line.color.rgb = COLOR_BLUE
        tag.line.width = Pt(1)
        tf_tag = tag.text_frame
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_t = tf_tag.paragraphs[0]
        p_t.text = tag_text.upper()
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(8.5)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_BLUE
        p_t.alignment = PP_ALIGN.CENTER

        # Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.82), Inches(11.7), Inches(0.55))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(21)
        p.font.bold = True
        p.font.color.rgb = COLOR_HEADER

        # Subtitle
        if subtitle_text:
            sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.42), Inches(11.7), Inches(0.35))
            tf_s = sub.text_frame
            tf_s.word_wrap = True
            tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle_text
            p_s.font.name = FONT_FAMILY
            p_s.font.size = Pt(11)
            p_s.font.color.rgb = COLOR_MUTED

    # Helper: Place image with precise matching container frame (Aspect Ratio 1024x463 = 2.2117)
    def add_framed_image(slide, img_path, left, top, width):
        # 1024 x 463 aspect ratio = 0.45215 height-to-width
        img_w = width
        img_h = width * (463.0 / 1024.0)
        
        # Outer container frame matching image with 0.06" neat padding
        pad = Inches(0.06)
        frame = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, 
            left - pad, 
            top - pad, 
            img_w + (pad * 2), 
            img_h + (pad * 2)
        )
        frame.fill.solid()
        frame.fill.fore_color.rgb = COLOR_CARD
        frame.line.color.rgb = COLOR_BORDER_STRONG
        frame.line.width = Pt(1.5)

        # Embedded image perfectly centered in frame
        slide.shapes.add_picture(img_path, left, top, width=img_w, height=img_h)
        return img_h + (pad * 2)

    # =========================================================================
    # SLIDE 1: Title & Hook
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_bg(slide1)

    # Hero Center Container
    add_card(slide1, Inches(1.0), Inches(0.9), Inches(11.333), Inches(5.7), COLOR_CARD, COLOR_BORDER_STRONG)

    # Category Pill
    badge = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.4), Inches(3.6), Inches(0.36))
    badge.fill.solid()
    badge.fill.fore_color.rgb = COLOR_BLUE_BG
    badge.line.color.rgb = COLOR_BLUE
    badge.line.width = Pt(1)
    tf_b = badge.text_frame
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
    p_b = tf_b.paragraphs[0]
    p_b.text = "SUPPLY CHAIN RESILIENCE • HACKATHON PITCH"
    p_b.font.name = FONT_FAMILY
    p_b.font.size = Pt(8.5)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_BLUE
    p_b.alignment = PP_ALIGN.CENTER

    # Project Title
    t_box = slide1.shapes.add_textbox(Inches(1.5), Inches(1.95), Inches(10.3), Inches(1.0))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "BasketShield AI"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = COLOR_HEADER

    # Punchy Subtitle in Plain English
    s_box = slide1.shapes.add_textbox(Inches(1.5), Inches(2.95), Inches(10.3), Inches(0.65))
    tf_s = s_box.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = "Protecting Everyday Consumer Prices & Manufacturing Costs from Global Shipping Shocks & the AI Chip Crunch"
    p_s.font.name = FONT_FAMILY
    p_s.font.size = Pt(15)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_SUBHEADER

    # 3 High-Impact Cards
    cards1 = [
        ("6,000 Catalog Products", "Tested across Groceries (Coffee, Oils), Electronics (iPhones, GPUs), and Tesla EVs.", COLOR_BLUE),
        ("Sub-15ms AI Optimization", "Replaces weeks of manual supplier calls with instant Google OR-Tools math solving.", COLOR_GREEN),
        ("Up to 85% Price Shock Absorbed", "Keeps grocery store prices steady instead of passing huge cost hikes to shoppers.", COLOR_BLUE)
    ]
    for i, (head, desc, col) in enumerate(cards1):
        c_left = Inches(1.5 + i * 3.55)
        add_card(slide1, c_left, Inches(3.8), Inches(3.3), Inches(1.35), COLOR_BG, COLOR_BORDER)
        tb_c = slide1.shapes.add_textbox(c_left + Inches(0.2), Inches(3.95), Inches(2.9), Inches(1.05))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
        p1 = tf_c.paragraphs[0]
        p1.text = head
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = col
        p2 = tf_c.add_paragraph()
        p2.space_before = Pt(4)
        p2.text = desc
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(9.2)
        p2.font.color.rgb = COLOR_BODY

    # Team Attribution Footer
    team_box = slide1.shapes.add_textbox(Inches(1.5), Inches(5.45), Inches(10.3), Inches(0.65))
    tf_t = team_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = "Team Lazy  •  Shrey Jaiswal  &  Navya Gupta"
    p_t.font.name = FONT_FAMILY
    p_t.font.size = Pt(12.5)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_HEADER

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "Open Source on GitHub: github.com/lazyshrey/basketshield  •  Includes Research Paper & Benchmark Suite"
    p_t2.font.name = FONT_FAMILY
    p_t2.font.size = Pt(9.5)
    p_t2.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 2: The Problem (Why Prices Are Skyrocketing)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_bg(slide2)
    add_header(slide2, "01. The Problem", 
               "Why Are Everyday Prices Suddenly Skyrocketing?", 
               "Global events hit specific raw parts and shipping routes, creating massive price spikes.")

    shocks = [
        ("🚢 Ships Blocked in the Red Sea", "+300% to +400% Freight Surge",
         "When ships cannot pass through the Suez Canal, they take a 14-day detour around Africa.\n\nShipping a single container jumped from $1,400 to over $5,900. Everyday goods like coffee beans, tea, and cooking oils get delayed and rack up huge port fees.",
         COLOR_RED, COLOR_RED_BG),
        ("⚡ Energy Crisis at Smelting Plants", "+30% Raw Packaging Cost",
         "Energy prices in Europe forced glass and aluminum factories to add huge energy surcharges.\n\nFor a can of soda or a glass coffee jar, the packaging alone makes up almost 45% of the total manufacturing cost.",
         COLOR_RED, COLOR_RED_BG),
        ("🧠 The 2026 AI Memory Squeeze", "+60% to +70% RAM Price Jump",
         "Big tech companies (Google, Microsoft, OpenAI) are buying up over 80% of all memory chip wafers for AI servers.\n\nBecause factories are focused on AI chips, regular phone and laptop RAM has become scarce, driving device prices up.",
         COLOR_RED, COLOR_RED_BG)
    ]

    for i, (title, highlight, text, col, col_bg) in enumerate(shocks):
        left = Inches(0.8 + i * 4.0)
        add_card(slide2, left, Inches(1.95), Inches(3.73), Inches(4.9), COLOR_CARD, COLOR_BORDER)

        # Highlight Stat Pill
        sb = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.2), Inches(2.15), Inches(3.33), Inches(0.6))
        sb.fill.solid()
        sb.fill.fore_color.rgb = col_bg
        sb.line.color.rgb = col
        sb.line.width = Pt(1)
        tf_sb = sb.text_frame
        tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
        p_sb = tf_sb.paragraphs[0]
        p_sb.text = highlight
        p_sb.font.name = FONT_FAMILY
        p_sb.font.size = Pt(11)
        p_sb.font.bold = True
        p_sb.font.color.rgb = col
        p_sb.alignment = PP_ALIGN.CENTER

        # Body
        tb = slide2.shapes.add_textbox(left + Inches(0.2), Inches(2.9), Inches(3.33), Inches(3.7))
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
        p2.text = text
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 3: The Gap (Why Spreadsheets Fail)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_bg(slide3)
    add_header(slide3, "02. The Failure Mode", 
               "Why Spreadsheets & Traditional ERPs Fail During Shocks", 
               "Companies don't have real-time optimization tools, so they pass 100% of the cost to consumers.")

    # Left Box: Traditional ERP
    add_card(slide3, Inches(0.8), Inches(1.95), Inches(5.65), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_l = slide3.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(5.05), Inches(4.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

    p_l = tf_l.paragraphs[0]
    p_l.text = "How Companies Handle Shocks Today (Old Way)"
    p_l.font.name = FONT_FAMILY
    p_l.font.size = Pt(14)
    p_l.font.bold = True
    p_l.font.color.rgb = COLOR_HEADER

    old_points = [
        ("❌ Slow Manual Calls (Takes 4 Weeks):", "When freight spikes, procurement managers take weeks calling and emailing other suppliers. By then, the price hike is already locked in."),
        ("❌ Blind to Raw Parts:", "Companies buy finished bottles or chips without knowing where the glass, aluminum, or wafers actually came from, making them blind to bottlenecks."),
        ("❌ Static Spreadsheets:", "Excel only shows historical averages. It cannot calculate complex trade-offs like tariffs vs. local shipping vs. recycling mandates.")
    ]
    for b_txt, d_txt in old_points:
        p_item = tf_l.add_paragraph()
        p_item.space_before = Pt(12)
        run_b = p_item.add_run()
        run_b.text = b_txt + "\n"
        run_b.font.name = FONT_FAMILY
        run_b.font.size = Pt(10)
        run_b.font.bold = True
        run_b.font.color.rgb = COLOR_RED
        run_d = p_item.add_run()
        run_d.text = d_txt
        run_d.font.name = FONT_FAMILY
        run_d.font.size = Pt(9.5)
        run_d.font.color.rgb = COLOR_BODY

    # Right Box: The Real Consequence
    add_card(slide3, Inches(6.85), Inches(1.95), Inches(5.65), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_r = slide3.shapes.add_textbox(Inches(7.15), Inches(2.2), Inches(5.05), Inches(4.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

    p_r = tf_r.paragraphs[0]
    p_r.text = "The Consequence for Everyday People"
    p_r.font.name = FONT_FAMILY
    p_r.font.size = Pt(14)
    p_r.font.bold = True
    p_r.font.color.rgb = COLOR_HEADER

    consequences = [
        ("💸 Grocery Checkout Inflation:", "Food and beverage brands run on tight 35% margins. If their packaging jumps 40%, they can't absorb it. They increase the shelf price at the supermarket."),
        ("📦 Shrinkflation at the Store:", "When brands fear losing customers from price hikes, they reduce the package size while charging the same price—giving you less product for your money."),
        ("🛡️ What BasketShield Changes:", "Instead of waiting weeks or raising prices, BasketShield AI solves the math in 15 milliseconds, immediately routing orders to cheaper domestic suppliers!")
    ]
    for b_txt, d_txt in consequences:
        p_item = tf_r.add_paragraph()
        p_item.space_before = Pt(12)
        run_b = p_item.add_run()
        run_b.text = b_txt + "\n"
        run_b.font.name = FONT_FAMILY
        run_b.font.size = Pt(10)
        run_b.font.bold = True
        run_b.font.color.rgb = COLOR_GREEN
        run_d = p_item.add_run()
        run_d.text = d_txt
        run_d.font.name = FONT_FAMILY
        run_d.font.size = Pt(9.5)
        run_d.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 4: How BasketShield Works (The 3-Step Solution)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_bg(slide4)
    add_header(slide4, "03. The Solution", 
               "How BasketShield AI Solves It in 3 Simple Steps", 
               "An automated workflow from raw product parts to sub-15ms mathematical optimization.")

    steps = [
        ("Step 1: Break Down the Product", "🔬 Physical Parts Decomposition",
         "BasketShield uses AI and physical catalogs to break down any product into its exact components:\n\n• For a coffee jar: 214g glass jar, 14.5g plastic lid, 0.8g foil seal, 100g coffee beans.\n• For a phone: Titanium body, display glass, and 8GB LPDDR5X RAM chips.\n\nNow we know exactly what materials are vulnerable.",
         COLOR_BLUE),
        ("Step 2: Track Global Shocks", "🌍 Live Crisis & Tariff Engine",
         "The platform tracks real-world disruption scenarios:\n\n• Red Sea and Suez shipping congestion.\n• European glass and aluminum gas tariffs.\n• AI memory wafer shortages at chip foundries.\n\nIt calculates how each shock affects individual raw materials in real time.",
         COLOR_RED),
        ("Step 3: Solve the Math in 15ms", "⚡ Google OR-Tools Optimizer",
         "Instead of human guesswork, Google OR-Tools runs a Mixed-Integer Linear Program (MILP) to find the best plan:\n\n• Selects the cheapest local and nearshore suppliers.\n• Bypasses import tariffs and expensive shipping routes.\n• Guarantees 70%+ recycled material usage.",
         COLOR_GREEN)
    ]

    for i, (step_num, title, body, col) in enumerate(steps):
        left = Inches(0.8 + i * 4.0)
        add_card(slide4, left, Inches(1.95), Inches(3.73), Inches(4.3), COLOR_CARD, COLOR_BORDER)

        # Step Pill
        sb = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.2), Inches(2.15), Inches(3.33), Inches(0.42))
        sb.fill.solid()
        sb.fill.fore_color.rgb = COLOR_BG
        sb.line.color.rgb = col
        sb.line.width = Pt(1)
        tf_sb = sb.text_frame
        tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
        p_sb = tf_sb.paragraphs[0]
        p_sb.text = step_num.upper()
        p_sb.font.name = FONT_FAMILY
        p_sb.font.size = Pt(9.5)
        p_sb.font.bold = True
        p_sb.font.color.rgb = col
        p_sb.alignment = PP_ALIGN.CENTER

        # Body
        tb = slide4.shapes.add_textbox(left + Inches(0.2), Inches(2.7), Inches(3.33), Inches(3.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(12.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_HEADER

        p2 = tf.add_paragraph()
        p2.space_before = Pt(6)
        p2.text = body
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(9.2)
        p2.font.color.rgb = COLOR_BODY

    # Flow Banner at Bottom
    add_card(slide4, Inches(0.8), Inches(6.4), Inches(11.73), Inches(0.65), COLOR_CARD, COLOR_BORDER)
    tb_b = slide4.shapes.add_textbox(Inches(1.0), Inches(6.45), Inches(11.3), Inches(0.55))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
    p_b = tf_b.paragraphs[0]
    p_b.text = "RESULT: Enterprise managers get the mathematically cheapest sourcing plan in under 15 milliseconds!"
    p_b.font.name = FONT_FAMILY
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_BLUE
    p_b.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 5: Live Demo — The Resilience Cockpit (Aligned Screenshot 1)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_bg(slide5)
    add_header(slide5, "04. Product Demo", 
               "The Resilience Cockpit: Simulating Shocks in Real Time", 
               "A clean, responsive dashboard where users can test 6,000 products against real-world trade crises.")

    # Left: Clear, Simple Takeaways
    add_card(slide5, Inches(0.8), Inches(1.95), Inches(4.3), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_c5 = slide5.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(3.8), Inches(4.5))
    tf_c5 = tb_c5.text_frame
    tf_c5.word_wrap = True
    tf_c5.margin_left = tf_c5.margin_top = tf_c5.margin_right = tf_c5.margin_bottom = 0

    p_c5 = tf_c5.paragraphs[0]
    p_c5.text = "What You Can Do on This Screen:"
    p_c5.font.name = FONT_FAMILY
    p_c5.font.size = Pt(13)
    p_c5.font.bold = True
    p_c5.font.color.rgb = COLOR_HEADER

    cockpit_points = [
        ("1. Pick Any Product (6,000 SKUs):", "Select from 3 sectors: Grocery (coffee, oils), Electronics (phones, GPUs), or Automotive (Tesla Model 3, Cybertruck)."),
        ("2. Toggle Live Crisis Scenarios:", "One-click simulation for the 2026 Red Sea detour, Taiwan Strait congestion, or smelting gas spikes."),
        ("3. Instant Material Identification:", "The app automatically detects packaging types (Glass Jar, Aluminum Can, Battery Pack) and links them to raw market prices.")
    ]
    for h_txt, b_txt in cockpit_points:
        p_item = tf_c5.add_paragraph()
        p_item.space_before = Pt(14)
        run_h = p_item.add_run()
        run_h.text = h_txt + "\n"
        run_h.font.name = FONT_FAMILY
        run_h.font.size = Pt(10)
        run_h.font.bold = True
        run_h.font.color.rgb = COLOR_BLUE
        run_b = p_item.add_run()
        run_b.text = b_txt
        run_b.font.name = FONT_FAMILY
        run_b.font.size = Pt(9.2)
        run_b.font.color.rgb = COLOR_BODY

    # Right: Screenshot 1 with Exact Math-Based Bounding Frame
    img1 = os.path.join(os.path.dirname(__file__), "screenshots", "01_resilience_cockpit_home.png")
    if os.path.exists(img1):
        # 7.2" width -> 3.25" height
        add_framed_image(slide5, img1, Inches(5.35), Inches(2.2), Inches(7.15))

    # Bottom Pill under Screenshot
    add_card(slide5, Inches(5.35), Inches(5.8), Inches(7.27), Inches(1.05), COLOR_BG, COLOR_BORDER)
    tb_pill = slide5.shapes.add_textbox(Inches(5.5), Inches(5.92), Inches(7.0), Inches(0.85))
    tf_pill = tb_pill.text_frame
    tf_pill.word_wrap = True
    tf_pill.margin_left = tf_pill.margin_top = tf_pill.margin_right = tf_pill.margin_bottom = 0
    p_pl = tf_pill.paragraphs[0]
    p_pl.text = "⚡ Real-Time Feedback:"
    p_pl.font.name = FONT_FAMILY
    p_pl.font.size = Pt(10)
    p_pl.font.bold = True
    p_pl.font.color.rgb = COLOR_HEADER
    p_pl2 = tf_pill.add_paragraph()
    p_pl2.text = "When you select a product like Davidoff Espresso 57, the cockpit immediately flags the '+14-day Cape detour' and calculates the exact price impact."
    p_pl2.font.name = FONT_FAMILY
    p_pl2.font.size = Pt(9.2)
    p_pl2.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 6: The Proof (Unit Economics & Cost Defense - Aligned Screenshot 2)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_bg(slide6)
    add_header(slide6, "05. The Proof", 
               "Defending the Landed Cost: A Real Example", 
               "Tested on a real grocery staple: Davidoff Espresso 57 Instant Glass Jar (100g).")

    # Left: Aligned Screenshot 2
    img2 = os.path.join(os.path.dirname(__file__), "screenshots", "02_physical_bom_cost_defense.png")
    if os.path.exists(img2):
        add_framed_image(slide6, img2, Inches(0.85), Inches(2.2), Inches(6.8))

    # Right: High-Impact Numbers Box
    add_card(slide6, Inches(7.9), Inches(1.95), Inches(4.6), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_res = slide6.shapes.add_textbox(Inches(8.15), Inches(2.15), Inches(4.1), Inches(4.5))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True
    tf_res.margin_left = tf_res.margin_top = tf_res.margin_right = tf_res.margin_bottom = 0

    p_r1 = tf_res.paragraphs[0]
    p_r1.text = "The Real Numbers (Unit Cost):"
    p_r1.font.name = FONT_FAMILY
    p_r1.font.size = Pt(13)
    p_r1.font.bold = True
    p_r1.font.color.rgb = COLOR_HEADER

    metrics = [
        ("Normal Base Cost:", "$0.50 / unit", "Standard packaging cost before the shipping and gas shock.", COLOR_HEADER),
        ("Unmitigated Crisis Shock:", "$1.03 / unit", "+105% cost spike! Double the packaging cost if you don't optimize.", COLOR_RED),
        ("Defended with BasketShield:", "$0.10 / unit", "-79.8% cost saved by immediately shifting orders to domestic suppliers.", COLOR_GREEN),
        ("Supermarket Store Price:", "$9.40 (Defended)", "Saves consumers $0.97 per jar! Keeps the price stable instead of jumping to $10.37.", COLOR_GREEN)
    ]
    for lbl, val, note, col in metrics:
        p_item = tf_res.add_paragraph()
        p_item.space_before = Pt(8)
        run_l = p_item.add_run()
        run_l.text = lbl + " "
        run_l.font.name = FONT_FAMILY
        run_l.font.size = Pt(9.5)
        run_l.font.bold = True
        run_l.font.color.rgb = COLOR_SUBHEADER
        run_v = p_item.add_run()
        run_v.text = val + "\n"
        run_v.font.name = FONT_FAMILY
        run_v.font.size = Pt(11)
        run_v.font.bold = True
        run_v.font.color.rgb = col
        run_n = p_item.add_run()
        run_n.text = note
        run_n.font.name = FONT_FAMILY
        run_n.font.size = Pt(8.5)
        run_n.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 7: Executive Summary in Plain English (Aligned Screenshot 3)
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_bg(slide7)
    add_header(slide7, "06. Executive Insights", 
               "Explaining Complex Math in Plain English", 
               "Managers don't want confusing equations—they want clear answers they can act on immediately.")

    # Left: 3 Clear Business Answers
    add_card(slide7, Inches(0.8), Inches(1.95), Inches(5.1), Inches(4.9), COLOR_CARD, COLOR_BORDER)
    tb_b7 = slide7.shapes.add_textbox(Inches(1.05), Inches(2.15), Inches(4.6), Inches(4.5))
    tf_b7 = tb_b7.text_frame
    tf_b7.word_wrap = True
    tf_b7.margin_left = tf_b7.margin_top = tf_b7.margin_right = tf_b7.margin_bottom = 0

    p_b7 = tf_b7.paragraphs[0]
    p_b7.text = "The 3 Questions Every Executive Asks:"
    p_b7.font.name = FONT_FAMILY
    p_b7.font.size = Pt(13)
    p_b7.font.bold = True
    p_b7.font.color.rgb = COLOR_HEADER

    questions = [
        ("1. What Broke in the Supply Chain?", "Shipping detours around Africa added 14 days of delays, and gas shortages spiked factory annealing costs for glass jars."),
        ("2. Why Would Shoppers Pay More?", "Food companies only make a 35% margin. When jar costs jump $0.53, they pass that cost down, hiking grocery bills."),
        ("3. How Did the Math Engine Fix It?", "Within 15ms, the optimizer switched orders to pre-qualified local suppliers, avoiding canal penalties and keeping 72% recycled content!")
    ]
    for q_t, a_t in questions:
        p_item = tf_b7.add_paragraph()
        p_item.space_before = Pt(10)
        run_q = p_item.add_run()
        run_q.text = q_t + "\n"
        run_q.font.name = FONT_FAMILY
        run_q.font.size = Pt(10)
        run_q.font.bold = True
        run_q.font.color.rgb = COLOR_BLUE
        run_a = p_item.add_run()
        run_a.text = a_t
        run_a.font.name = FONT_FAMILY
        run_a.font.size = Pt(9.2)
        run_a.font.color.rgb = COLOR_BODY

    # Right: Aligned Screenshot 3
    img3 = os.path.join(os.path.dirname(__file__), "screenshots", "03_executive_decision_brief.png")
    if os.path.exists(img3):
        add_framed_image(slide7, img3, Inches(6.15), Inches(2.2), Inches(6.35))

    # Bottom Callout on Right
    add_card(slide7, Inches(6.15), Inches(5.4), Inches(6.47), Inches(1.45), COLOR_BG, COLOR_BORDER)
    tb_call = slide7.shapes.add_textbox(Inches(6.35), Inches(5.5), Inches(6.1), Inches(1.25))
    tf_call = tb_call.text_frame
    tf_call.word_wrap = True
    tf_call.margin_left = tf_call.margin_top = tf_call.margin_right = tf_call.margin_bottom = 0
    p_c1 = tf_call.paragraphs[0]
    p_c1.text = "🎯 Why Judges & Executives Love This:"
    p_c1.font.name = FONT_FAMILY
    p_c1.font.size = Pt(10)
    p_c1.font.bold = True
    p_c1.font.color.rgb = COLOR_GREEN
    p_c2 = tf_call.add_paragraph()
    p_c2.space_before = Pt(3)
    p_c2.text = "Instead of an opaque black-box AI or a generic dashboard, BasketShield delivers transparent mathematical proof alongside clear human explanations."
    p_c2.font.name = FONT_FAMILY
    p_c2.font.size = Pt(9.2)
    p_c2.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 8: Wrap-Up, Impact & Team Lazy
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_bg(slide8)
    add_header(slide8, "07. Wrap-Up & Team", 
               "Project Impact, Open Source & Team Lazy", 
               "Everything built in this project is verified, open-source, and ready to deploy.")

    summary_boxes = [
        ("⚡ Proven Performance", "Measurable Results",
         "• Sub-15ms Solve Time: Runs live in the browser without freezing.\n\n• Up to 85% Price Shock Absorbed: Defends unit costs across 6,000 products.\n\n• 100% Automated Test Pass: All edge cases and boundary tests verified.",
         COLOR_BLUE),
        ("📦 Complete Open Source", "Audit-Ready Deliverables",
         "• Live Streamlit Cockpit: 4 clean pages, dark-mode shadcn/ui design.\n\n• Peer-Audited Research Paper: Full PDF whitepaper included.\n\n• GitHub Repository: Clean 8-commit conventional history at github.com/lazyshrey/basketshield.",
         COLOR_BLUE),
        ("👥 Team Lazy", "Project Creators",
         "• Team Name: Team Lazy\n\n• Members:\n  - Shrey Jaiswal\n  - Navya Gupta\n\n• Built With:\n  Python, Google OR-Tools, Gemini AI,\n  Streamlit, Plotly & python-pptx.\n\n• License: Open Source (MIT)",
         COLOR_GREEN)
    ]

    for i, (title, sub, body, col) in enumerate(summary_boxes):
        left = Inches(0.8 + i * 4.0)
        add_card(slide8, left, Inches(1.95), Inches(3.73), Inches(4.9), COLOR_CARD, COLOR_BORDER)

        sb = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.2), Inches(2.15), Inches(3.33), Inches(0.42))
        sb.fill.solid()
        sb.fill.fore_color.rgb = COLOR_BG
        sb.line.color.rgb = col
        sb.line.width = Pt(1)
        tf_sb = sb.text_frame
        tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
        p_sb = tf_sb.paragraphs[0]
        p_sb.text = sub.upper()
        p_sb.font.name = FONT_FAMILY
        p_sb.font.size = Pt(9.5)
        p_sb.font.bold = True
        p_sb.font.color.rgb = col
        p_sb.alignment = PP_ALIGN.CENTER

        tb = slide8.shapes.add_textbox(left + Inches(0.2), Inches(2.7), Inches(3.33), Inches(3.9))
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

    # Save Presentation locally and in Downloads
    local_pptx = os.path.join(os.path.dirname(__file__), "BasketShield_AI_Presentation.pptx")
    prs.save(local_pptx)
    print(f"Presentation saved locally to: {local_pptx}")

    downloads_dir = r"C:\Users\5apri\Downloads"
    if os.path.exists(downloads_dir):
        # Also save a fresh copy under BasketShield_AI_Hackathon_Pitch.pptx in case user has original open in PowerPoint
        fallback_pptx = os.path.join(downloads_dir, "BasketShield_AI_Hackathon_Pitch.pptx")
        shutil.copy2(local_pptx, fallback_pptx)
        print(f"Presentation saved to Downloads as: {fallback_pptx}")
        try:
            downloads_pptx = os.path.join(downloads_dir, "BasketShield_AI_Presentation.pptx")
            shutil.copy2(local_pptx, downloads_pptx)
            print(f"Presentation overwritten in Downloads: {downloads_pptx}")
        except PermissionError:
            print("Notice: BasketShield_AI_Presentation.pptx is currently locked/open in PowerPoint. Saved as BasketShield_AI_Hackathon_Pitch.pptx")

if __name__ == "__main__":
    create_deck()
