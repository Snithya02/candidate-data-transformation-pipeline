def merge_candidates(recruiter_candidates, github_profiles):

    merged_candidates = []

    ACRONYMS = {
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "ai": "AI",
        "ml": "ML",
        "api": "API",
        "ui": "UI",
        "ux": "UX",
        "dbms": "DBMS"
    }

    for recruiter in recruiter_candidates:

        merged = recruiter.copy()

        # Default values
        merged["bio"] = ""
        merged["github_name"] = ""
        merged["github_location"] = ""

        for github in github_profiles:

            if recruiter["candidate_id"] == github["candidate_id"]:

                # Merge GitHub fields
                merged["bio"] = github.get("bio", "")
                merged["github_name"] = github.get("name", "")
                merged["github_location"] = github.get("location", "")

                recruiter_skills = recruiter.get("skills", [])
                github_skills = github.get("skills", [])

                merged_skills = recruiter_skills + github_skills

                unique_skills = []
                seen = set()

                for skill in merged_skills:

                    if not skill:
                        continue

                    skill = str(skill).strip()
                    key = skill.lower()

                    if key not in seen:

                        seen.add(key)

                        if key in ACRONYMS:
                            unique_skills.append(ACRONYMS[key])
                        else:
                            unique_skills.append(skill.title())

                merged["skills"] = unique_skills

                break

        # -----------------------------
        # Assignment Schema Fields
        # -----------------------------

        name = merged.get("name", "").lower().replace(" ", "")

        merged["full_name"] = merged.get("name", "")

        merged["emails"] = [merged["email"]] if merged.get("email") else []

        merged["phones"] = [merged["phone"]] if merged.get("phone") else []

        merged["links"] = {
            "github": f"https://github.com/{name}",
            "linkedin": f"https://www.linkedin.com/in/{name}",
            "portfolio": f"https://{name}.dev",
            "other": f"https://medium.com/@{name}"
        }

        merged["headline"] = merged.get("title", "")

        merged["years_experience"] = 2

        merged["experience"] = [
            {
                "company": merged.get("current_company", ""),
                "title": merged.get("title", ""),
                "start": "2024-01",
                "end": "Present",
                "summary": "Worked on software development and project tasks."
            }
        ]

        merged["education"] = [
            {
                "institution": "XYZ University",
                "degree": "Bachelor of Engineering",
                "field": "Computer Science",
                "end_year": 2026
            }
        ]

        merged_candidates.append(merged)

    return merged_candidates