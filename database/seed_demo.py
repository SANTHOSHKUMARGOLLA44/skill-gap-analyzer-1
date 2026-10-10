"""Create the demo account and sample assessment. Run after initializing the database."""
from app import app, init_db, DATABASE
import sqlite3
from werkzeug.security import generate_password_hash
from datetime import datetime
import json
from app import ROLE_REQUIREMENTS
from services.skill_gap import analyze_gaps
from services.readiness import calculate_readiness
from services.roadmap import generate_roadmap

def seed():
    init_db()
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    existing = conn.execute("SELECT id FROM students WHERE email='demo@example.com'").fetchone()
    if existing:
        print("Demo account already exists: demo@example.com / DemoPass123!")
        conn.close()
        return
    now = datetime.utcnow().isoformat()
    cur = conn.execute("""INSERT INTO students(full_name,email,password_hash,college,branch,academic_year,graduation_year,target_role,created_at)
                          VALUES(?,?,?,?,?,?,?,?,?)""",
                       ("Demo Student","demo@example.com",generate_password_hash("DemoPass123!"),
                        "Sample College","Computer Science","3","2027","Software Developer",now))
    sid = cur.lastrowid
    scores = {"Python":75,"Java":60,"DSA":35,"SQL":50,"Aptitude":68}
    gaps = analyze_gaps(scores, ROLE_REQUIREMENTS["Software Developer"])
    readiness = calculate_readiness(scores, 1, 1,
        {"full_name":"Demo Student","college":"Sample College","branch":"Computer Science","graduation_year":"2027"})
    cur = conn.execute("INSERT INTO assessments(student_id,target_role,scores_json,gaps_json,readiness_score,created_at) VALUES(?,?,?,?,?,?)",
                       (sid,"Software Developer",json.dumps(scores),json.dumps(gaps),readiness["score"],now))
    aid = cur.lastrowid
    for row in gaps:
        conn.execute("INSERT INTO skills(student_id,assessment_id,skill_name,proficiency,required_score,gap,priority) VALUES(?,?,?,?,?,?,?)",
                     (sid,aid,row["skill"],row["current"],row["required"],row["gap"],row["priority"]))
    conn.execute("INSERT INTO projects(student_id,title,description,skills,created_at) VALUES(?,?,?,?,?)",
                 (sid,"Student Management System","A CRUD application to practice core development.","Python, SQL",now))
    conn.execute("INSERT INTO certifications(student_id,title,issuer,created_at) VALUES(?,?,?,?)",
                 (sid,"Python Fundamentals","Sample Learning Platform",now))
    for task in generate_roadmap(gaps,"Software Developer"):
        conn.execute("""INSERT INTO recommendations(student_id,assessment_id,kind,title,description,skill_name,week_number,priority,estimated_hours,completed)
                        VALUES(?,?,?,?,?,?,?,?,?,0)""",
                     (sid,aid,"roadmap",task["title"],task["description"],task["skill"],task["week"],task["priority"],task["hours"]))
    conn.commit()
    conn.close()
    print("Demo account created: demo@example.com / DemoPass123!")

if __name__ == "__main__":
    seed()
