import pandas as pd


def normalize_skills(skills):

    if pd.isna(skills):
        return []

    skills = str(skills).split(",")

    cleaned = []
    seen = set()

    ACRONYMS = {
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "ai": "AI",
        "ml": "ML",
        "api": "API",
        "ui": "UI",
        "ux": "UX",
        "dbms": "DBMS",
        "rest api": "REST API"
    }

    for skill in skills:

        skill = skill.strip()

        if skill == "":
            continue

        key = skill.lower()

        if key in ACRONYMS:
            skill = ACRONYMS[key]
        else:
            skill = skill.title()

        if key not in seen:
            seen.add(key)
            cleaned.append(skill)

    return cleaned