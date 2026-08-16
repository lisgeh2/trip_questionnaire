"""The questionnaire itself.

Everything the survey asks lives here, so you can change the questions without
touching any Streamlit code.

A question is a dict with:
    key      unique id -- also the field name in the saved answers
    label    the text shown to the user
    type     "text" | "textarea" | "radio" | "multiselect" | "slider"
    options  list of choices          (radio / multiselect only)
    min/max  bounds                   (slider only)
    default  starting position        (slider only, defaults to `min`)
    required whether it must be filled in (default: True)
"""

PAGES = [
    {
        "title": "Briefing",
        "intro": "So you want to trip on mushrooms or consider it.",
        "questions": [
            {
                "key": "full_name",
                "label": "Your name",
                "type": "text",
            },
            {
                "key": "age",
                "label": "Your age",
                "type": "slider",
                "min": 16,
                "max": 99,
                "default": 30,
            },
            {
                "key": "country",
                "label": "Where do you live?",
                "type": "radio",
                "options": ["Switzerland", "Germany", "Austria", "Other"],
            },
        ],
    },
    {
        "title": "Your work",
        "intro": "Tell us a bit about what you do day to day.",
        "questions": [
            {
                "key": "role",
                "label": "What best describes your role?",
                "type": "radio",
                "options": ["Student", "Engineer", "Researcher", "Manager", "Other"],
            },
            {
                "key": "tools",
                "label": "Which tools do you use regularly?",
                "type": "multiselect",
                "options": ["Python", "R", "Excel", "SQL", "Power BI", "None of these"],
            },
            {
                "key": "years_experience",
                "label": "Years of experience",
                "type": "slider",
                "min": 0,
                "max": 40,
                "default": 5,
            },
        ],
    },
    {
        "title": "Feedback",
        "intro": "Last page. Then you can submit.",
        "questions": [
            {
                "key": "satisfaction",
                "label": "How satisfied are you with your current tooling? (1 = awful, 10 = great)",
                "type": "slider",
                "min": 1,
                "max": 10,
                "default": 5,
            },
            {
                "key": "biggest_pain",
                "label": "What slows you down the most?",
                "type": "textarea",
            },
            {
                "key": "comments",
                "label": "Anything else you want to add?",
                "type": "textarea",
                "required": False,
            },
        ],
    },
]


def all_questions():
    """Every question across all pages, in order."""
    return [question for page in PAGES for question in page["questions"]]


def question_keys():
    """All question keys, in order."""
    return [question["key"] for question in all_questions()]
