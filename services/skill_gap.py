def analyze_gaps(scores, requirements):
    """Return role-specific gaps sorted from largest to smallest."""
    rows = []
    for skill, required in requirements.items():
        current = float(scores.get(skill, 0))
        gap = round(max(0.0, float(required) - current), 1)
        if gap == 0:
            priority = "Target met"
        elif gap >= 30:
            priority = "High"
        elif gap >= 10:
            priority = "Medium"
        else:
            priority = "Low"
        rows.append({"skill": skill, "current": round(current, 1), "required": float(required),
                     "gap": gap, "priority": priority})
    return sorted(rows, key=lambda x: (-x["gap"], x["skill"]))
