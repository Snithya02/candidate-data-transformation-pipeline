def add_provenance(candidate):

    provenance = {}

    if candidate.get("name"):
        provenance["name"] = "Recruiter CSV"

    if candidate.get("email"):
        provenance["email"] = "Recruiter CSV"

    if candidate.get("phone"):
        provenance["phone"] = "Recruiter CSV"

    if candidate.get("skills"):
        provenance["skills"] = "Recruiter CSV + GitHub"

    if candidate.get("bio"):
        provenance["bio"] = "GitHub"

    if candidate.get("github_name"):
        provenance["github_name"] = "GitHub"

    if candidate.get("github_location"):
        provenance["github_location"] = "GitHub"

    return provenance