PROJECTS = {
    "Software Developer": [
        {"title":"Student Management System","description":"Build CRUD flows for student records with validation and search.","skills":["Python","SQL","Web Development"],"difficulty":"Beginner","duration":"1–2 weeks"},
        {"title":"Online Examination System","description":"Create quizzes, scoring, user roles, and result history.","skills":["Java","SQL","Problem Solving"],"difficulty":"Intermediate","duration":"2–3 weeks"},
        {"title":"Task Management Application","description":"Build task lists, filters, status updates, and a responsive UI.","skills":["Python","JavaScript","SQL"],"difficulty":"Intermediate","duration":"2 weeks"},
    ],
    "Data Analyst": [
        {"title":"Student Performance Dashboard","description":"Explore student results and visualize trends and distributions.","skills":["Python","Statistics","Data Visualization"],"difficulty":"Beginner","duration":"1–2 weeks"},
        {"title":"Sales Data Analysis","description":"Clean a dataset, answer business questions, and summarize insights.","skills":["SQL","Statistics","Python"],"difficulty":"Intermediate","duration":"2 weeks"},
        {"title":"Data Visualization Dashboard","description":"Create interactive charts and explain key metrics.","skills":["SQL","Data Visualization"],"difficulty":"Intermediate","duration":"2–3 weeks"},
    ],
    "Cybersecurity Analyst": [
        {"title":"Log Analysis Dashboard","description":"Parse sample logs and flag unusual patterns in a safe lab dataset.","skills":["Python","Linux","Security Fundamentals"],"difficulty":"Intermediate","duration":"2 weeks"},
        {"title":"Password Strength Checker","description":"Evaluate password strength locally and explain safe password practices.","skills":["Python","Security Fundamentals"],"difficulty":"Beginner","duration":"3–5 days"},
        {"title":"Network Security Learning Lab","description":"Document a controlled local lab and analyze sample network events.","skills":["Networking","Linux"],"difficulty":"Intermediate","duration":"2–3 weeks"},
    ],
}
def recommend_projects(role, gaps):
    candidates = PROJECTS.get(role, PROJECTS["Software Developer"])
    gap_skills = [g["skill"] for g in gaps if g.get("gap", 0) > 0]
    result = []
    for p in candidates:
        overlap = [s for s in p["skills"] if s in gap_skills]
        result.append({**p, "reason": f"Builds {', '.join(overlap)} skills related to your current gaps." if overlap else "Builds practical experience for your selected role."})
    result.sort(key=lambda p: -sum(s in gap_skills for s in p["skills"]))
    return result
