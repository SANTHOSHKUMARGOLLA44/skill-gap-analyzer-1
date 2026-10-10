CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    college TEXT DEFAULT '',
    branch TEXT DEFAULT '',
    academic_year TEXT DEFAULT '',
    graduation_year TEXT DEFAULT '',
    target_role TEXT NOT NULL DEFAULT 'Software Developer',
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    assessment_id INTEGER NOT NULL,
    skill_name TEXT NOT NULL,
    proficiency REAL NOT NULL CHECK(proficiency BETWEEN 0 AND 100),
    required_score REAL NOT NULL CHECK(required_score BETWEEN 0 AND 100),
    gap REAL NOT NULL CHECK(gap BETWEEN 0 AND 100),
    priority TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT DEFAULT '',
    skills TEXT DEFAULT '',
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS certifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    issuer TEXT DEFAULT '',
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS job_roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT DEFAULT ''
);
CREATE TABLE IF NOT EXISTS job_requirements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_id INTEGER NOT NULL REFERENCES job_roles(id) ON DELETE CASCADE,
    skill_name TEXT NOT NULL,
    required_score REAL NOT NULL CHECK(required_score BETWEEN 0 AND 100),
    UNIQUE(role_id, skill_name)
);
CREATE TABLE IF NOT EXISTS assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    target_role TEXT NOT NULL,
    scores_json TEXT NOT NULL,
    gaps_json TEXT NOT NULL,
    readiness_score REAL NOT NULL CHECK(readiness_score BETWEEN 0 AND 100),
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    assessment_id INTEGER REFERENCES assessments(id) ON DELETE CASCADE,
    kind TEXT NOT NULL DEFAULT 'roadmap',
    title TEXT NOT NULL,
    description TEXT DEFAULT '',
    skill_name TEXT DEFAULT '',
    week_number INTEGER DEFAULT 1,
    priority TEXT DEFAULT 'Medium',
    estimated_hours INTEGER DEFAULT 2,
    completed INTEGER NOT NULL DEFAULT 0 CHECK(completed IN (0,1)),
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    skill_name TEXT DEFAULT '',
    old_score REAL,
    new_score REAL,
    note TEXT DEFAULT '',
    created_at TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS quiz_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    target_role TEXT NOT NULL,
    selected_skills_json TEXT NOT NULL,
    answers_json TEXT NOT NULL,
    results_json TEXT NOT NULL,
    score REAL NOT NULL DEFAULT 0,
    total_questions INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL
);
