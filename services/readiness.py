WEIGHTS = {
    "Programming Skills": 20, "DSA": 20, "SQL": 15, "Aptitude": 15,
    "Projects": 15, "Certifications / Internships": 5, "Resume / Profile Completeness": 10
}

def calculate_readiness(scores, projects_count=0, certifications_count=0, profile=None):
    """Calculate a transparent weighted readiness score.
    Missing technical components are scored as 0 rather than silently receiving full marks.
    Projects and certifications use simple capped evidence scores; profile completeness uses 4 fields.
    """
    # sqlite3.Row supports key lookup but not dict.get(); normalize it first.
    profile = dict(profile) if profile is not None else {}
    programming_values = [scores[k] for k in ("Python", "Java") if k in scores]
    programming = sum(programming_values) / len(programming_values) if programming_values else 0
    profile_fields = ["full_name", "college", "branch", "graduation_year"]
    profile_score = sum(1 for f in profile_fields if str(profile.get(f, "") or "").strip()) / len(profile_fields) * 100
    components = {
        "Programming Skills": programming,
        "DSA": float(scores.get("DSA", 0)),
        "SQL": float(scores.get("SQL", 0)),
        "Aptitude": float(scores.get("Aptitude", 0)),
        "Projects": min(100, projects_count * 25),
        "Certifications / Internships": min(100, certifications_count * 50),
        "Resume / Profile Completeness": profile_score
    }
    weighted = sum(components[name] * weight / 100 for name, weight in WEIGHTS.items())
    return {"score": round(max(0, min(100, weighted)), 1),
            "components": {k: round(v, 1) for k, v in components.items()},
            "weights": WEIGHTS,
            "note": "Project-defined metric, not a prediction of employment. Missing technical scores count as 0."}
