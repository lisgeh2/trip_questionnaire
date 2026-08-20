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