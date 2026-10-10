def generate_roadmap(gaps, role):
    """Create a practical starter roadmap ordered around the largest skill gaps."""
    top = [g for g in gaps if g["gap"] > 0][:2]
    focus = top[0]["skill"] if top else "Interview Practice"
    gap_skills = [g["skill"] for g in top]
    templates = {
        "DSA": [
            ("DSA Basics", "Arrays, strings, searching, and time/space complexity.", 4),
            ("Core DSA", "Sorting, linked lists, stacks, queues, and practice problems.", 5),
            ("Intermediate DSA", "Trees, hashing, recursion, and intermediate problems.", 5),
            ("Interview Practice", "Mixed problems, timed coding tests, mock interviews, and revision.", 4),
        ],
        "SQL": [
            ("SQL Foundations", "SELECT, filtering, sorting, aggregate functions, and constraints.", 3),
            ("Joins and Grouping", "Practice joins, GROUP BY, HAVING, and multi-table queries.", 4),
            ("Subqueries and Design", "Subqueries, CTEs, normalization, and query reasoning.", 4),
            ("SQL Interview Practice", "Solve timed SQL questions and review query performance basics.", 3),
        ],
        "Python": [
            ("Python Foundations", "Review data types, control flow, functions, and collections.", 3),
            ("Problem Solving", "Practice functions, files, exceptions, and small coding exercises.", 4),
            ("OOP and Libraries", "Use classes and relevant libraries through mini-projects.", 4),
            ("Python Interview Practice", "Solve timed questions and explain your solutions.", 3),
        ],
        "Java": [
            ("Java Foundations", "Review syntax, collections, methods, and exception handling.", 3),
            ("Object-Oriented Java", "Practice inheritance, interfaces, encapsulation, and polymorphism.", 4),
            ("Collections and DSA", "Use collections and solve common data-structure problems.", 4),
            ("Java Interview Practice", "Solve timed problems and review common interview topics.", 3),
        ],
        "Aptitude": [
            ("Aptitude Basics", "Review percentages, ratios, averages, and number systems.", 3),
            ("Reasoning Practice", "Practice series, arrangements, directions, and logical reasoning.", 4),
            ("Timed Sets", "Solve mixed quantitative and reasoning questions under time limits.", 4),
            ("Mock Test and Review", "Take a timed test and review mistakes by topic.", 3),
        ],
    }
    generic = [
        (f"{focus} Foundations", f"Learn the core concepts of {focus} and complete beginner exercises.", 3),
        (f"{focus} Practice", f"Work through guided exercises and small tasks in {focus}.", 4),
        (f"{focus} Applied Skills", f"Build a small practical exercise using {focus}.", 4),
        ("Review and Mock Practice", f"Review {focus} and practice role-related interview questions.", 3),
    ]
    primary = templates.get(focus, generic)
    tasks = []
    for week, (title, desc, hours) in enumerate(primary, 1):
        tasks.append({"title": title, "description": desc, "skill": focus, "week": week,
                      "priority": "High" if week <= 2 else "Medium", "hours": hours})
    if len(gap_skills) > 1:
        second = gap_skills[1]
        tasks.append({"title": f"Next focus: {second}", "description": f"Start targeted practice for {second} after completing the first focus area.",
                      "skill": second, "week": 5, "priority": "Medium", "hours": 3})
    return tasks
