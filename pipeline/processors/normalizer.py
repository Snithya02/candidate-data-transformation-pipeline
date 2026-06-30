from pipeline.processors.name_normalizer import normalize_name
from pipeline.processors.email_normalizer import normalize_email
from pipeline.processors.phone_normalizer import normalize_phone
from pipeline.processors.skill_normalizer import normalize_skills


def normalize_candidate(candidate):

    candidate["name"] = normalize_name(candidate.get("name"))

    candidate["email"] = normalize_email(candidate.get("email"))

    candidate["phone"] = normalize_phone(candidate.get("phone"))

    candidate["skills"] = normalize_skills(candidate.get("skills"))

    return candidate