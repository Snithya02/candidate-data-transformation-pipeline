def calculate_confidence(candidate):

    score = 0

    # 1. Recruiter record quality (30)
    if candidate.get("email"):
        score += 10

    if candidate.get("phone"):
        score += 5

    if candidate.get("current_company"):
        score += 5

    if candidate.get("title"):
        score += 5

    if candidate.get("location"):
        score += 5

    # 2. Skills quality (30)
    skills = candidate.get("skills", [])

    if len(skills) >= 8:
        score += 30
    elif len(skills) >= 6:
        score += 25
    elif len(skills) >= 4:
        score += 20
    elif len(skills) >= 2:
        score += 15
    elif len(skills) >= 1:
        score += 10

    # 3. GitHub enrichment (40)
    if candidate.get("github_name"):
        score += 15

    if candidate.get("bio"):
        score += 15

    if candidate.get("github_location"):
        score += 10

    return min(score, 100)