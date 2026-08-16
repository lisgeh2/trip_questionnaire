"""A small questionnaire app: log in, answer three pages, submit.

Run it with:

    streamlit run app.py
"""

from __future__ import annotations

import json

import streamlit as st

import auth
import storage
from questions import PAGES, all_questions, question_keys

# Every answer is stored in st.session_state under this prefix, e.g. "q_age".
ANSWER_PREFIX = "q_"

st.set_page_config(page_title="Questionnaire", page_icon="📝")


# --------------------------------------------------------------------------
# Session state
# --------------------------------------------------------------------------
def init_state() -> None:
    """Set up the keys the app relies on (only the first time)."""
    st.session_state.setdefault("username", None)
    st.session_state.setdefault("page_index", 0)
    st.session_state.setdefault("submitted", False)

    # Sliders need a starting position; the other widgets are happy empty.
    for question in all_questions():
        if question["type"] == "slider":
            default = question.get("default", question["min"])
            st.session_state.setdefault(ANSWER_PREFIX + question["key"], default)


def keep_answers_alive() -> None:
    """Streamlit forgets a widget's value once the widget is no longer drawn.

    Re-assigning each answer to itself at the start of every run marks it as
    "still in use", so answers survive switching between pages.
    """
    for key in list(st.session_state.keys()):
        if key.startswith(ANSWER_PREFIX):
            st.session_state[key] = st.session_state[key]


def collect_answers() -> dict:
    """All answers as a plain dict: {question key: value}."""
    return {key: st.session_state.get(ANSWER_PREFIX + key) for key in question_keys()}


def is_answered(value) -> bool:
    """Empty string, empty list and None all count as unanswered."""
    return value not in (None, "", [])


def missing_on_page(page: dict) -> list[str]:
    """Labels of the required questions on this page that are still empty."""
    return [
        question["label"]
        for question in page["questions"]
        if question.get("required", True)
        and not is_answered(st.session_state.get(ANSWER_PREFIX + question["key"]))
    ]


# --------------------------------------------------------------------------
# Callbacks (they run before the page is redrawn, which is what we want)
# --------------------------------------------------------------------------
def go_to_page(index: int) -> None:
    st.session_state.page_index = index


def log_out() -> None:
    st.session_state.clear()


def start_over() -> None:
    for key in list(st.session_state.keys()):
        if key.startswith(ANSWER_PREFIX):
            del st.session_state[key]
    st.session_state.page_index = 0
    st.session_state.submitted = False


# --------------------------------------------------------------------------
# Screens
# --------------------------------------------------------------------------
def login_screen() -> None:
    st.title("📝 Questionnaire")
    st.write("Please log in to continue.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in")

    if submitted:
        if auth.check_credentials(username, password):
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Unknown user or wrong password.")

    st.caption(f"Demo account: `{auth.DEMO_USER[0]}` / `{auth.DEMO_USER[1]}`")


def render_sidebar() -> None:
    """The standard Streamlit sidebar: who you are, where you are, progress."""
    with st.sidebar:
        st.write(f"Logged in as **{st.session_state.username}**")
        st.button("Log out", on_click=log_out, use_container_width=True)
        st.divider()

        # The radio writes straight into page_index, so clicking a page name
        # and clicking "Next" end up doing exactly the same thing.
        st.radio(
            "Pages",
            options=range(len(PAGES)),
            format_func=lambda i: f"{i + 1}. {PAGES[i]['title']}",
            key="page_index",
            disabled=st.session_state.submitted,
        )
        st.divider()

        answers = collect_answers()
        done = sum(is_answered(value) for value in answers.values())
        st.progress(done / len(answers), text=f"{done} of {len(answers)} answered")
        st.caption(f"Answers are saved to `{storage.DATA_FILE}`")


def render_question(question: dict) -> None:
    """Draw one widget. Its value lives in session_state under `key`."""
    key = ANSWER_PREFIX + question["key"]
    label = question["label"]
    kind = question["type"]

    if kind == "text":
        st.text_input(label, key=key)
    elif kind == "textarea":
        st.text_area(label, key=key)
    elif kind == "radio":
        st.radio(label, question["options"], index=None, key=key)
    elif kind == "multiselect":
        st.multiselect(label, question["options"], key=key)
    elif kind == "slider":
        st.slider(label, question["min"], question["max"], key=key)
    else:
        raise ValueError(f"Unknown question type: {kind!r}")


def render_questionnaire() -> None:
    index = st.session_state.page_index
    page = PAGES[index]
    is_last_page = index == len(PAGES) - 1

    st.title(page["title"])
    st.caption(f"Page {index + 1} of {len(PAGES)}")
    if page.get("intro"):
        st.write(page["intro"])

    for question in page["questions"]:
        render_question(question)

    st.divider()
    left, right = st.columns(2)

    with left:
        st.button(
            "← Back",
            disabled=index == 0,
            use_container_width=True,
            on_click=go_to_page,
            args=(index - 1,),
        )

    with right:
        if is_last_page:
            if st.button("Submit ✓", type="primary", use_container_width=True):
                submit()
        else:
            st.button(
                "Next →",
                type="primary",
                use_container_width=True,
                on_click=go_to_page,
                args=(index + 1,),
            )

    # A gentle nudge, not a blocker -- you can still browse the other pages.
    missing = missing_on_page(page)
    if missing:
        st.info("Still open on this page: " + ", ".join(missing))


def submit() -> None:
    """Validate everything, then hand the answers to storage.py."""
    unanswered = [label for page in PAGES for label in missing_on_page(page)]
    if unanswered:
        st.error("Please answer these first: " + ", ".join(unanswered))
        return

    storage.save_response(st.session_state.username, collect_answers())
    st.session_state.submitted = True
    st.rerun()


def render_thank_you() -> None:
    st.title("Thanks! 🎉")
    st.success(f"Your answers were saved to `{storage.DATA_FILE}`.")

    answers = collect_answers()
    with st.expander("Show what you submitted"):
        st.json(answers)

    st.download_button(
        "Download my answers (JSON)",
        data=json.dumps(answers, indent=2, ensure_ascii=False),
        file_name="my_answers.json",
        mime="application/json",
    )
    st.button("Fill in another response", on_click=start_over)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main() -> None:
    auth.ensure_demo_user()
    init_state()
    keep_answers_alive()

    if st.session_state.username is None:
        login_screen()
        return

    render_sidebar()
    if st.session_state.submitted:
        render_thank_you()
    else:
        render_questionnaire()


main()
