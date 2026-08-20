from colors import MULTIPLE_COLORS, CORE_COLOR, BACKGROUND, FARBEN_4_ABSTUFUNGEN, FARBEN_4
from config import STYLE

def give_html(color, farben, height_css, flex_css):
    if STYLE == "gfs":
        return f"""<style>
    .stat-card.accent-{color} {{
        --card:   #FFFFFF;
        --border: {farben['sehr_dunkel']};
        --accent: {farben['sehr_dunkel']};
        --text:   {farben['dunkel']};
        --muted:  {farben['hell']};

        background: var(--card);
        border: 5px solid var(--border);
        border-radius: 8px;
        padding: 1.75rem 2rem;
        position: relative;
        overflow: hidden;
        font-family: "DM Sans", -apple-system, sans-serif;
        color: var(--text);
        {height_css};
        {flex_css};
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15),
                    0 2px 4px rgba(0, 0, 0, 0.13);
    }}
    .stat-card.accent-{color}::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: var(--accent);
    }}
    .stat-card.accent-{color} .stat-label       {{ color: var(--muted); }}
    .stat-card.accent-{color} .stat-description {{ color: var(--muted); }}
    .stat-card.accent-{color} .percent          {{ color: var(--muted); }}
    .stat-card.accent-{color} .stat-number {{ text-align: center; }}
    </style>"""

    if STYLE == "cool_black":
        return f"""<style>
    .stat-card.accent-{color} {{
        --accent: {farben['basis']};
        --glow:   {farben['dunkel']};
        --text:   {farben['sehr_dunkel']};
        --muted:  rgba(234, 240, 255, 0.45);

        background: linear-gradient(150deg,
                    {farben['sehr_hell']} 0%,
                    rgba(5, 6, 10, 0) 55%);
        border: 1px solid rgba(234, 240, 255, 0.10);
        border-left: 3px solid var(--accent);
        border-radius: 2px;
        padding: 1.75rem 2rem;
        position: relative;
        overflow: hidden;
        font-family: "Archivo", "Inter", -apple-system, sans-serif;
        color: var(--text);
        {height_css};
        {flex_css};
        box-shadow: none;
    }}
    .stat-card.accent-{color}::before {{
        content: "";
        position: absolute;
        top: -60%; right: -30%;
        width: 70%; height: 200%;
        background: radial-gradient(closest-side, var(--accent), transparent);
        opacity: 0.16;
        filter: blur(28px);
        pointer-events: none;
    }}
    .stat-card.accent-{color} .section-title {{
        color: var(--accent);
        border-bottom: 1px solid rgba(234, 240, 255, 0.10);
        opacity: 0.9;
    }}
    .stat-card.accent-{color} .stat-label       {{ color: var(--muted); }}
    .stat-card.accent-{color} .stat-description {{ color: var(--muted); }}
    .stat-card.accent-{color} .percent {{
        color: var(--accent);
        text-shadow: 0 0 18px var(--accent);
    }}
    .stat-card.accent-{color} .stat-number {{
        text-align: left;
        color: var(--text);
        text-shadow: 0 0 34px {farben['hell']};
    }}
    </style>"""

    if STYLE == "leavy":
        return f"""<style>
    .stat-card.accent-{color} {{
        --card:   #fdfaf3;
        --rule:   {farben['dunkel']};
        --accent: {farben['basis']};
        --text:   {farben['sehr_dunkel']};
        --muted:  {farben['dunkel']};

        background: var(--card);
        border: 1px solid var(--rule);
        border-radius: 0;
        padding: 2rem 2.25rem 1.75rem 2.25rem;
        position: relative;
        overflow: hidden;
        font-family: "EB Garamond", Georgia, serif;
        color: var(--text);
        {height_css};
        {flex_css};
        justify-content: center;
        gap: 0.2rem;
        box-shadow: inset 0 0 0 1px var(--card),
                    inset 0 0 0 4px var(--rule),
                    0 18px 34px -12px rgba(34, 32, 27, 0.42),
                    0 4px 10px rgba(34, 32, 27, 0.18);
    }}
    .stat-card.accent-{color}::before {{
        content: "";
        position: absolute;
        top: 18px; left: 50%;
        transform: translateX(-50%);
        width: 34px; height: 1px;
        background: var(--accent);
        opacity: 0.55;
    }}
    .stat-card.accent-{color}::after {{
        content: "";
        position: absolute;
        right: -70px; bottom: -80px;
        width: 190px; height: 190px;
        border: 1px solid var(--accent);
        border-radius: 50%;
        opacity: 0.10;
        pointer-events: none;
    }}
    .stat-card.accent-{color} .section-title {{
        color: var(--muted);
        border-bottom: 1px solid {farben['sehr_hell']};
        text-align: center;
        font-size: 0.66rem;
        letter-spacing: 0.20em;
    }}
    .stat-card.accent-{color} .stat-label       {{ color: var(--muted); }}
    .stat-card.accent-{color} .stat-description {{
        color: var(--muted);
        text-align: center;
        font-style: italic;
        max-width: 32ch;
        margin-left: auto;
        margin-right: auto;
    }}
    .stat-card.accent-{color} .percent {{
        color: var(--accent);
        font-style: italic;
    }}
    .stat-card.accent-{color} .stat-number {{
        text-align: center;
        color: var(--accent);
    }}
    </style>"""

    if STYLE == "comic_brutalist":
        return f"""<style>
    .stat-card.accent-{color} {{
        --paper:  #f4f1e8;
        --ink:    #14161a;
        --accent: {farben['basis']};

        background: var(--paper);
        border: 4px solid var(--ink);
        border-radius: 0;
        padding: 0 1.6rem 1.4rem 1.6rem;
        position: relative;
        overflow: hidden;
        font-family: "Archivo", Helvetica, sans-serif;
        color: var(--ink);
        {height_css};
        {flex_css};
        box-shadow: 9px 9px 0 0 var(--accent),
                    9px 9px 0 4px var(--ink);
    }}
    /* Halbtonfeld, unten links, wie ein Rasterdruck */
    .stat-card.accent-{color}::before {{
        content: "";
        position: absolute;
        left: 0; bottom: 0;
        width: 46%; height: 42%;
        background-image: radial-gradient(var(--ink) 1.4px, transparent 1.5px);
        background-size: 9px 9px;
        opacity: 0.16;
        pointer-events: none;
    }}
    /* Farbblock, der die rechte Kante sprengt */
    .stat-card.accent-{color}::after {{
        content: "";
        position: absolute;
        top: 0; right: 0;
        width: 26px; height: 54%;
        background: var(--accent);
        border-left: 4px solid var(--ink);
        pointer-events: none;
    }}
    /* Label als schwarzer Streifen, der an der Oberkante klebt */
    .stat-card.accent-{color} .section-title {{
        display: block;
        background: var(--ink);
        color: var(--paper);
        border-bottom: none;
        margin: 0 -1.6rem 1.1rem -1.6rem;
        padding: 9px 1.6rem;
        font-family: "JetBrains Mono", monospace;
        font-size: 0.62rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        position: relative;
        z-index: 1;
    }}
    .stat-card.accent-{color} .stat-label {{ color: var(--ink); }}
    .stat-card.accent-{color} .stat-description {{
        font-family: "JetBrains Mono", monospace;
        font-size: 0.72rem;
        line-height: 1.5;
        color: var(--ink);
        opacity: 0.75;
        text-align: left;
        max-width: 34ch;
        position: relative;
        z-index: 1;
    }}
    .stat-card.accent-{color} .percent {{
        color: var(--accent);
        -webkit-text-stroke: 2px var(--ink);
        margin-left: 0.02em;
    }}
    .stat-card.accent-{color} .stat-number {{
        text-align: left;
        color: var(--accent);
        -webkit-text-stroke: 3px var(--ink);
        paint-order: stroke fill;
        position: relative;
        z-index: 1;
    }}
    </style>"""


def big_number(area, column, column_text, number, text, color="rot", add_percent=True, height = None):
    farben = FARBEN_4_ABSTUFUNGEN[color]
    if height:
        height = str(height)+"px"

    cls = f"stat-card accent-{color}"

    if add_percent:
        area.html(
            f'<div class="{cls}">'
            f'<div class="section-title">{column} · {column_text}</div>'
            f'<p class="stat-number">{number}<span class="percent">%</span></p>'
            f'<p class="stat-description">{text}</p>'
            '</div>'
        )
    else:
        area.html(
            f'<div class="{cls}">'
            f'<div class="section-title">{column} · {column_text}</div>'
            f'<p class="stat-number">{number}</p>'
            f'<p class="stat-description">{text}</p>'
            '</div>'
        )

    height_css = ""
    flex_css = ""
    
    if height is not None:
        height_css = f"height: {height};"
        flex_css = """display: flex;
        flex-direction: column;
        justify-content: space-between;"""
    
    html = give_html(color, farben, height_css, flex_css)
    area.html(html)