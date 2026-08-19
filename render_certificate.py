"""Makes the certificate for one person.

    python render_certificate.py <token>     writes certificate_<username>.html
    python render_certificate.py             lists the tokens

The html is self-contained - no images, no css files - so it can be moved,
mailed or handed to someone as a single file.
"""

import sys
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import process_responses as pr

BASE_DIR = Path(__file__).parent

TOLERANCE = 0.12   # the +/- around the dose. 1.9 g -> 1.7-2.2 g
SCALE_MAX = 3.5    # right end of the little ruler under the dose, in grams

SCREENING_LABELS = {
    "ok": "Cleared",
    "maybe": "Cleared, with something to discuss",
    "no": "Not cleared",
}

# same items give_screening_result() checks, with something readable to show
SCREENING_ITEMS = [
    ("bipolar_self", "Mania or bipolar disorder — you"),
    ("bipolar_family", "Mania or bipolar disorder — family"),
    ("schizophrenia_self", "Schizophrenia — you"),
    ("schizophrenia_family", "Schizophrenia — family"),
]

DOSE_FACTORS = [
    ("Sensitivity",
     "Your own reports on weed, psychedelics and medication in general, weighted by how much you have to go on",
     pr.sensitvity_dose_factor),
    ("Absorption",
     "Higher trait absorption tends to need less",
     pr.absorption_dose_factor),
    ("Body weight",
     "Measured against a 71 kg reference",
     pr.weight_dose_factor),
]

PREFERENCE_ITEMS = [
    ("alone_preference", "Being alone"),
    ("touch_preference", "Touch"),
    ("setting_preference", "Setting"),
    ("other_preferences", "Anything else"),
]

REFLECTION_ITEMS = [
    ("concerns", "What still concerns you"),
    ("goals", "What you would like to work with"),
    ("last_comments", "Your last comments"),
]


def medication_note(reasons):
    """give_screening_result() glues its reasons together. The per-item ones are
    already shown as flags, so strip them and keep the medication text."""
    for key, text in SCREENING_ITEMS:
        reasons = reasons.replace("You answered yes to " + key, " ")
    return " ".join(reasons.split())


def build_dose(token):
    base = pr.give_base_dose(token)
    total = pr.give_final_dosing(token)
    value = round(total, 1)
    low = round(total * (1 - TOLERANCE), 1)
    high = round(total * (1 + TOLERANCE), 1)

    factors = []
    for name, explanation, factor_function in DOSE_FACTORS:
        factor = factor_function(token)
        factors.append({
            "name": name,
            "explanation": explanation,
            "percent": f"{factor*100:+.1f}%",
            "grams": f"{base*factor:+.2f} g",
        })

    return {
        "value": f"{value:.1f}",
        "low": f"{low:.1f}",
        "high": f"{high:.1f}",
        "base": f"{base:.2f}",
        "exact": f"{total:.2f}",
        "tolerance": f"{int(TOLERANCE*100)}%",
        "factors": factors,
        "scale": {
            "low": min(100, low / SCALE_MAX * 100),
            "high": min(100, high / SCALE_MAX * 100),
            "point": min(100, value / SCALE_MAX * 100),
            "ticks": [{"label": g, "position": g / SCALE_MAX * 100} for g in (0, 1, 2, 3)],
        },
    }


def build_summary(answers, medication):
    """The important answers on one page. Absorption, screening and the
    preferences have their own sections above, so they are not repeated."""
    groups = [
        {"title": "Experience", "rows": [
            {"label": "Cannabis", "value": answers["weed_experience"].capitalize()},
            {"label": "Psychedelics", "value": answers["psych_experience"].capitalize()},
            {"label": "Self-rated sensitivity", "value":
                f"weed {answers['weed_sensitivity']}/10 · "
                f"psychedelics {answers['psych_sensitivity']}/10 · "
                f"medication in general {answers['other_sensitivity']}/10"},
        ]},
        {"title": "You", "rows": [
            {"label": "Desired intensity", "value": f"{answers['dose_preference']}/10"},
            {"label": "Body weight", "value": f"{answers['body_weight']} kg"},
            {"label": "Medication", "value": medication.capitalize() or "None reported"},
            {"label": "Readiness", "value":
                f"{answers['readiness1']}/10 before, {answers['readiness2']}/10 after"},
        ]},
    ]

    if answers["active_recall_demon"].strip():
        groups.append({"title": "Your plan", "rows": [
            {"label": "If something frightening turns up",
             "value": answers["active_recall_demon"].strip()},
        ]})

    return groups


def build_context(token):
    user_record = next((r for r in pr.responses if r["token"] == token), None)
    if user_record is None:
        sys.exit("No response with that token. Run the script with no arguments to list them.")

    answers = user_record["answers"]
    result, reasons = pr.give_screening_result(token)

    context = {
        "username": user_record["username"],
        "token_short": token[:8],
        "submitted_at": datetime.fromisoformat(user_record["submitted_at"]).strftime("%d %B %Y"),
        "generated_at": datetime.now().strftime("%d %B %Y"),
        "screening": {
            "result": result,
            "label": SCREENING_LABELS[result],
            "color": pr.give_screening_hex(token),
            "cleared": result in ("ok", "maybe"),
            "flags": [text for key, text in SCREENING_ITEMS if answers[key] == "yes"],
            "notes": medication_note(reasons),
        },
    }

    # a "no" stops here: no dose, no preferences, no summary
    if not context["screening"]["cleared"]:
        return context

    delta = pr.readiness_int(token)

    context["readiness"] = {
        "before": answers["readiness1"],
        "after": answers["readiness2"],
        "delta": delta,
        "sentence": pr.readiness_text(token),
        "direction": "up" if delta > 0 else "down" if delta < 0 else "flat",
    }
    context["dose"] = build_dose(token)
    context["absorption"] = {
        "text": pr.absorption_text(token),
        "average": f"{pr.calculate_average(['absorption1', 'absorption2', 'absorption3'], token=token):.1f}",
    }
    context["preferences"] = [
        {"label": label, "value": answers[key],
         "unsure": answers[key].strip().lower() == "i dont know"}
        for key, label in PREFERENCE_ITEMS if answers[key].strip()
    ]
    context["reflections"] = [
        {"label": label, "value": answers[key].strip()}
        for key, label in REFLECTION_ITEMS if answers[key].strip()
    ]
    context["summary"] = build_summary(answers, answers["meds_interaction_text"].strip())

    return context


def render(token):
    env = Environment(
        loader=FileSystemLoader(str(BASE_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env.get_template("certificate.html").render(**build_context(token))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        for record in pr.responses:
            print(record["token"], record["username"])
    else:
        token = sys.argv[1]
        username = next(r["username"] for r in pr.responses if r["token"] == token)
        out_file = BASE_DIR / f"certificate_{username}.html"
        out_file.write_text(render(token), encoding="utf-8")
        print("Wrote", out_file)