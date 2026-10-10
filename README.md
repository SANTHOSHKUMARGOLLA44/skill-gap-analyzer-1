# AI-Powered Student Skill-Gap & Placement Readiness Analyzer

A Flask + SQLite web application that compares a student's proficiency with role-specific requirements, calculates a transparent project-defined readiness score, creates a focused learning roadmap, recommends projects, and tracks reassessments.

## Features
- Student registration, login, and profile editing
- Three target roles: Software Developer, Data Analyst, Cybersecurity Analyst
- Role-specific skill-gap analysis and priority sorting
- Weighted placement-readiness score with component breakdown
- Dashboard with Chart.js visualizations
- Four-week focused learning roadmap with persistent task completion
- Project and certification tracking
- Historical assessments and progress view
- Sample demo account

## Requirements
- Python 3.10+
- Windows, macOS, or Linux
- VS Code recommended

## Run on Windows (PowerShell)
```powershell
cd skill_gap_analyzer
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "from app import init_db; init_db()"
python app.py
```

To create the optional demo account manually, run `python database/seed_demo.py` after installing dependencies and initializing the database.
Open http://127.0.0.1:5000 in your browser.

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal and activate again. You can also install packages with `.venv\Scripts\python.exe -m pip install -r requirements.txt`.

## Run on macOS/Linux
```bash
cd skill_gap_analyzer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "from app import init_db; init_db()"
python app.py
```

To create the optional demo account manually, run `python database/seed_demo.py` after installing dependencies and initializing the database.

## Demo
Click **Try demo dashboard** on the homepage. The sample account uses:
- Email: `demo@example.com`
- Password: `DemoPass123!`

The demo-login shortcut signs into the sample account directly for quick presentations. Use the normal registration flow for a new account.

## Readiness score methodology
The overall score uses the presentation's weights:
- Programming Skills 20%
- DSA 20%
- SQL 15%
- Aptitude 15%
- Projects 15%
- Certifications / Internships 5%
- Resume / Profile Completeness 10%

Programming Skills is the mean of Python and Java where present. Project evidence is capped at 25 points per recorded project, certification/internship evidence at 50 points per recorded certification, and profile completeness is based on name, college, branch, and graduation year. Missing technical components score 0. This is a project-defined metric, not a prediction of employment.

## Skill gap rules
`gap = max(0, required_score - current_score)`.
- High: 30 points or more
- Medium: 10–29 points
- Low: 1–9 points
- Target met: 0 points

## Database
The SQLite file is created at `database/skill_gap.db` when `init_db()` is run. Tables include students, skills, projects, certifications, job roles, job requirements, assessments, recommendations, and progress.

## Security notes
- Set a unique `SECRET_KEY` environment variable before deployment.
- This is a college project starter. Before public production deployment, add CSRF protection, rate limiting, email verification, hardened session-cookie settings, and deployment-specific security review.
- Do not run Flask debug mode on a public server.
- Resume upload/AI extraction is intentionally left as an optional future extension; the core app requires no paid API.

## Tests
```bash
python -m unittest discover -s tests -v
```

## Updated Course Analyzer and Admin Console

The updated app includes a Course Analyzer workflow:
1. Sign in as a student.
2. Open **Course Analyzer** in the left navigation.
3. Select a target role and one or more skills.
4. Complete the generated multiple-choice test.
5. Review the overall score, per-skill performance, explanations for missed answers, and improvement priorities. Attempts are saved to SQLite.

### Admin monitoring
- Open `http://127.0.0.1:5000/admin/login`
- Default local demo credentials: `admin@example.com` / `AdminPass123!`
- The admin dashboard displays registered students, skill-assessment counts, Course Analyzer attempts, recent test scores, and project counts.
- For a local deployment, set `ADMIN_EMAIL` and `ADMIN_PASSWORD` before first starting the app to choose the initial admin credentials. The admin account is created during database initialization; changing these environment variables does not reset an already-created account.
- Change `SECRET_KEY` and the default admin password before any public deployment. The admin console is intended as a local project demo and should be hardened before internet exposure.

### If you already have an older database
The application uses `CREATE TABLE IF NOT EXISTS` to add the new `quiz_attempts` and `admins` tables when it starts. Restart with `python app.py` from the inner `skill_gap_analyzer` directory.
