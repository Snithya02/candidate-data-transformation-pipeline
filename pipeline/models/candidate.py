class Candidate:

    def __init__(self):

        self.candidate_id = ""

        self.full_name = ""

        self.email = ""

        self.phone = ""

        self.skills = []

        self.location = ""

        self.github = ""

        self.headline = ""

        self.years_experience = 0

        self.confidence = 0

        self.provenance = {}

        self.warnings = []

        self.sources = []

    def to_dict(self):

        return {

            "candidate_id": self.candidate_id,

            "full_name": self.full_name,

            "email": self.email,

            "phone": self.phone,

            "skills": self.skills,

            "location": self.location,

            "github": self.github,

            "headline": self.headline,

            "years_experience": self.years_experience,

            "confidence": self.confidence,

            "provenance": self.provenance,

            "warnings": self.warnings,

            "sources": self.sources

        }