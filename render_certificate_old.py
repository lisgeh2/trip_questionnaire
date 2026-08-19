"""Render the preparation certificate for one questionnaire response.

Usage:
    python render_certificate.py <token>              # writes certificate_<username>.html
    python render_certificate.py <token> -o out.html
    python render_certificate.py --list               # show tokens in the database

The screening PNG is read off disk and embedded in the HTML, so the certificate is
one self-contained file you can move or send anywhere. Use --images-dir if the
images live somewhere unusual, or --link-images to keep a plain relative <img src>.

All numbers come from process_responses.py. Nothing is recalculated here except
the confidence interval around the dose and the rounding for display.

NOTE: four functions in process_responses.py are currently broken in ways that
would show wrong information on the certificate. Every workaround below is
marked with "BUG:" and can be deleted once the source is fixed.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import sys
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import process_responses as pr

BASE_DIR = Path(__file__).parent
TEMPLATE_NAME = "certificate.html"

# Width of the interval drawn around the recommended dose (+/- 12%).
# 1.7 g -> 1.5-1.9 g
DOSE_TOLERANCE = 0.12

# Upper end of the printed dose scale, in grams.
DOSE_SCALE_MAX = 3.5

SCREENING_ITEMS = [
    ("bipolar_self", "Mania or bipolar disorder — you"),
    ("bipolar_family", "Mania or bipolar disorder — family"),
    ("schizophrenia_self", "Schizophrenia — you"),
    ("schizophrenia_family", "Schizophrenia — family"),
]

# BUG: give_screening_image() and give_screening_hex() test for result == "yes",
# but give_screening_result() returns "ok". An "ok" result therefore comes back
# as the red screening_no.png. These are the intended pairings.
SCREENING_ASSETS = {
    "ok": ("images/screening_yes.png", "#469c48", "Cleared"),
    "maybe": ("images/screening_maybe.png", "#faab06", "Cleared, with something to discuss"),
    "no": ("images/screening_no.png", "#ea1416", "Not cleared"),
}

PREFERENCE_FIELDS = [
    ("alone_preference", "Being alone", "How present the sitter should be"),
    ("touch_preference", "Touch", "Hand holding, a hand on the back, a hug"),
    ("setting_preference", "Setting", "Where you would like to be"),
    ("other_preferences", "Anything else", "In your words"),
]

# The preference answers are full sentences. The summary repeats them a screen
# later, so it uses these short forms instead of printing the same paragraph twice.
SHORT_FORMS = {
    "I would like to not be left alone at all, unless I specifically say so":
        "Never alone, unless she says so",
    "I dont care too much if the trip sitter goes away to grab something to eat, but I will communicate if I change my mind":
        "Fine if the sitter steps away briefly",
    "I am very fine with being alone, maybe I even want that. I know that I can always ask the trip sitter for company":
        "Happy alone, will ask for company",
    "I dont like being touched at all, unless I specifically say so":
        "No touch, unless asked for",
    "I am okay with touch, if it feels right in the moment. I know I can communicate in both directions":
        "Touch okay if it fits the moment",
    "I enjoy this kind of touch. I will communicate if I dont like something.":
        "Welcomes touch",
    "i dont know": "Undecided — worth talking through",
    "somewhere else that I will tell the tripsitter": "Somewhere else, to be told",
}


def short_form(value: str) -> str:
    return sentence_case(SHORT_FORMS.get(str(value).strip(), str(value).strip()))


def sentence_case(value: str) -> str:
    """Uppercase the first letter only — summary values read as labels, not prose."""
    value = str(value).strip()
    return value[:1].upper() + value[1:] if value else value


REFLECTION_FIELDS = [
    ("concerns", "What still concerns you"),
    ("goals", "What you would like to work with"),
    ("last_comments", "Your last comments"),
]


# --------------------------------------------------------------------------
# data access
# --------------------------------------------------------------------------

def get_record(token: str) -> dict:
    for record in pr.responses:
        if record["token"] == token:
            return record
    raise SystemExit(f"No response found for token {token!r}. Run with --list to see the tokens.")


def format_date(raw: str) -> str:
    try:
        return datetime.fromisoformat(raw).strftime("%d %B %Y")
    except (TypeError, ValueError):
        return raw


# --------------------------------------------------------------------------
# images
# --------------------------------------------------------------------------

def find_image(relative_path: str, images_dir: str | None = None) -> Path | None:
    """Look for the screening PNG in the places it plausibly lives."""
    name = Path(relative_path).name
    candidates = []
    if images_dir:
        candidates += [Path(images_dir) / name, Path(images_dir) / relative_path]
    candidates += [
        BASE_DIR / relative_path,
        BASE_DIR / "static" / relative_path,
        BASE_DIR / "full_database" / relative_path,
        BASE_DIR / name,
        Path.cwd() / relative_path,
        Path.cwd() / name,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def embed_image(relative_path: str, images_dir: str | None = None) -> str:
    """Return a data: URI for the image, or the original path if it can't be found."""
    found = find_image(relative_path, images_dir)
    if found is None:
        print(
            f"warning: could not find {relative_path!r}. Looked next to "
            f"{BASE_DIR}, in ./static, and in the current directory. The certificate "
            f"will link to it instead of embedding it — pass --images-dir to point at "
            f"the right folder.",
            file=sys.stderr,
        )
        return relative_path
    mime = mimetypes.guess_type(found.name)[0] or "image/png"
    encoded = base64.b64encode(found.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


# --------------------------------------------------------------------------
# sections
# --------------------------------------------------------------------------

def build_screening(token: str, answers: dict) -> dict:
    result, reasons = pr.give_screening_result(token)

    # Prefer the source functions, and correct them while they are still wrong.
    # Once the "yes"/"ok" mismatch is fixed this branch stops firing on its own.
    image = pr.give_screening_image(token)
    color = pr.give_screening_hex(token)
    expected_image, expected_color, label = SCREENING_ASSETS.get(result, SCREENING_ASSETS["no"])
    if image != expected_image:
        image, color = expected_image, expected_color

    # give_screening_result() concatenates its reasons without separators, and the
    # per-item ones repeat information we already show as flags. Strip those out and
    # keep whatever the medication check added.
    notes = reasons
    for key, _ in SCREENING_ITEMS:
        notes = notes.replace(f"You answered yes to {key}", " ")
    notes = " ".join(notes.split())

    flags = [label for key, label in SCREENING_ITEMS if answers.get(key) == "yes"]

    return {
        "result": result,
        "label": label,
        "image": image,
        "color": color,
        "flags": flags,
        "notes": notes,
        "medication": answers.get("meds_interaction_text", "").strip(),
        "cleared": result in ("ok", "maybe"),
    }


def build_readiness(token: str, answers: dict) -> dict:
    before = answers["readiness1"]
    after = answers["readiness2"]
    delta = pr.readiness_int(token)

    # BUG: readiness_text() calls readiness_int() without passing the token, so it
    # reads the default record instead of this one (and raises when that token is
    # missing from the database). Same wording, correct record.
    try:
        sentence = pr.readiness_text(token)
        describes_this_person = (
            ("same" in sentence) if delta == 0 else (f"by {delta}" in sentence)
        )
        if not describes_this_person:
            raise ValueError
    except (StopIteration, TypeError, ValueError):
        if delta == 0:
            sentence = "stayed the same."
        elif delta > 0:
            sentence = f"has increased by {delta}. Yay!"
        else:
            sentence = f"has decreased by {abs(delta)}."

    return {
        "before": before,
        "after": after,
        "delta": delta,
        "sentence": sentence,
        "direction": "up" if delta > 0 else ("down" if delta < 0 else "flat"),
    }


def build_dose(token: str) -> dict:
    base = pr.give_base_dose(token)
    sensitivity = pr.sensitvity_dose_factor(token)
    absorption = pr.absorption_dose_factor(token)
    weight = pr.weight_dose_factor(token)

    # BUG: give_final_dosing() passes the token to give_base_dose() but calls the
    # three factor functions with no argument, so it mixes this person's base dose
    # with the default record's adjustments. Same formula, one token throughout.
    total = base + (base * sensitivity) + (base * absorption) + (base * weight)

    value = round(total, 1)
    low = round(total * (1 - DOSE_TOLERANCE), 1)
    high = round(total * (1 + DOSE_TOLERANCE), 1)

    def factor_row(name: str, explanation: str, factor: float) -> dict:
        return {
            "name": name,
            "explanation": explanation,
            "percent": f"{factor * 100:+.1f}%",
            "grams": f"{base * factor:+.2f} g",
        }

    return {
        "value": f"{value:.1f}",
        "low": f"{low:.1f}",
        "high": f"{high:.1f}",
        "exact": f"{total:.2f}",
        "base": f"{base:.2f}",
        "tolerance": f"{int(DOSE_TOLERANCE * 100)}%",
        "factors": [
            factor_row(
                "Sensitivity",
                "Your own reports on weed, psychedelics and medication in general, weighted by how much you have to go on",
                sensitivity,
            ),
            factor_row(
                "Absorption",
                "Higher trait absorption tends to need less",
                absorption,
            ),
            factor_row(
                "Body weight",
                "Measured against a 71 kg reference",
                weight,
            ),
        ],
        "scale": {
            "low": min(100.0, low / DOSE_SCALE_MAX * 100),
            "high": min(100.0, high / DOSE_SCALE_MAX * 100),
            "point": min(100.0, value / DOSE_SCALE_MAX * 100),
            "ticks": [
                {"label": f"{g:g}", "position": g / DOSE_SCALE_MAX * 100}
                for g in (0, 1, 2, 3)
            ],
        },
    }


def build_absorption(token: str) -> dict:
    average = pr.calculate_average(["absorption1", "absorption2", "absorption3"], token=token)
    # BUG: absorption_text() compares a probability (0-1) against 40 and 60, so the
    # first branch can never be true and everyone is told they scored high. Left as
    # it is here on purpose — the fix belongs in process_responses.py.
    return {"text": pr.absorption_text(token), "average": f"{average:.1f}"}


def build_preferences(answers: dict) -> list[dict]:
    out = []
    for key, label, hint in PREFERENCE_FIELDS:
        value = str(answers.get(key, "")).strip()
        if not value:
            continue
        out.append({"label": label, "hint": hint, "value": value,
                    "unsure": value.strip().lower() in ("i dont know", "i don't know")})
    return out


def build_reflections(answers: dict) -> list[dict]:
    return [
        {"label": label, "value": str(answers.get(key, "")).strip()}
        for key, label in REFLECTION_FIELDS
        if str(answers.get(key, "")).strip()
    ]


def build_summary(answers: dict, screening: dict, readiness: dict, absorption: dict) -> list[dict]:
    experience = [
        {"label": "Cannabis", "value": sentence_case(answers["weed_experience"])},
        {"label": "Psychedelics", "value": sentence_case(answers["psych_experience"])},
        {"label": "Self-rated sensitivity", "value":
            f"weed {answers['weed_sensitivity']}/10 · psychedelics {answers['psych_sensitivity']}/10 · "
            f"medication in general {answers['other_sensitivity']}/10"},
    ]

    # Trait absorption and the screening verdict have their own sections above,
    # so they are deliberately not repeated here.
    body = [
        {"label": "Desired intensity", "value": f"{answers['dose_preference']}/10"},
        {"label": "Body weight", "value": f"{answers['body_weight']} kg"},
        {"label": "Medication", "value": sentence_case(screening["medication"]) or "None reported"},
        {"label": "Readiness", "value": f"{readiness['before']}/10 before, {readiness['after']}/10 after"},
    ]

    day = [
        {"label": "Sitter presence", "value": short_form(answers["alone_preference"])},
        {"label": "Touch", "value": short_form(answers["touch_preference"])},
        {"label": "Setting", "value": short_form(answers["setting_preference"])},
    ]

    # Goals are quoted in full a screen earlier, so only the bad-moment plan is repeated here.
    plan = []
    if str(answers.get("active_recall_demon", "")).strip():
        plan.append({"label": "If something frightening turns up",
                     "value": answers["active_recall_demon"].strip()})

    groups = [
        {"title": "Experience", "rows": experience},
        {"title": "You", "rows": body},
        {"title": "On the day", "rows": day},
    ]
    if plan:
        groups.append({"title": "Your plan", "rows": plan})
    return groups


# --------------------------------------------------------------------------
# render
# --------------------------------------------------------------------------

def build_context(token: str, images_dir: str | None = None, embed: bool = True) -> dict:
    record = get_record(token)
    answers = record["answers"]

    screening = build_screening(token, answers)
    if embed:
        screening["image"] = embed_image(screening["image"], images_dir)

    context = {
        "username": record["username"],
        "token": token,
        "token_short": token[:8],
        "submitted_at": format_date(record.get("submitted_at", "")),
        "generated_at": datetime.now(timezone.utc).strftime("%d %B %Y"),
        "screening": screening,
        "answers": answers,
    }

    if not screening["cleared"]:
        return context

    readiness = build_readiness(token, answers)
    absorption = build_absorption(token)
    context.update({
        "readiness": readiness,
        "dose": build_dose(token),
        "absorption": absorption,
        "preferences": build_preferences(answers),
        "reflections": build_reflections(answers),
        "summary": build_summary(answers, screening, readiness, absorption),
    })
    return context


def render(token: str, images_dir: str | None = None, embed: bool = True) -> str:
    env = Environment(
        loader=FileSystemLoader(str(BASE_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env.get_template(TEMPLATE_NAME).render(**build_context(token, images_dir, embed))


def main() -> None:
    parser = argparse.ArgumentParser(description="Render one preparation certificate.")
    parser.add_argument("token", nargs="?", help="Token of the response to render")
    parser.add_argument("-o", "--out", help="Output file (default certificate_<username>.html, - for stdout)")
    parser.add_argument("--images-dir", help="Folder holding the screening PNGs")
    parser.add_argument("--link-images", action="store_true",
                        help="Link the screening PNG instead of embedding it")
    parser.add_argument("--list", action="store_true", help="List tokens in the database and exit")
    args = parser.parse_args()

    if args.list:
        for record in pr.responses:
            print(f"{record['token']}  {record['username']}")
        return

    if not args.token:
        parser.error("give a token, or --list to see them")

    html = render(args.token, args.images_dir, embed=not args.link_images)

    if args.out == "-":
        sys.stdout.write(html)
        return

    out = Path(args.out) if args.out else BASE_DIR / f"certificate_{get_record(args.token)['username']}.html"
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()




