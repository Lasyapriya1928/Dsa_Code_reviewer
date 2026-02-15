import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "submissions.db")


# -----------------------------
# Initialize DB
# -----------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem_name TEXT,
            code TEXT,
            predicted_efficiency TEXT,
            predicted_pattern TEXT,
            big_o TEXT,
            explanation TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Save Submission
# -----------------------------
def save_submission(
    problem_name,
    predicted_efficiency,
    predicted_pattern,
    explanation_list,
    code
):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    explanation_text = " | ".join(explanation_list)

    cursor.execute("""
        INSERT INTO submissions (
            problem_name,
            predicted_efficiency,
            predicted_pattern,
            explanation,
            code,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        problem_name,
        predicted_efficiency,
        predicted_pattern,
        explanation_text,
        code,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


# -----------------------------
# Get All Submissions
# -----------------------------
def get_all_submissions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, problem_name, code,
               predicted_efficiency,
               predicted_pattern,
               big_o,
               explanation,
               timestamp
        FROM submissions
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    results = []

    for row in rows:
        results.append({
            "id": row[0],
            "problem_name": row[1],
            "code": row[2],
            "predicted_efficiency": row[3],
            "predicted_pattern": row[4],
            "big_o": row[5],
            "explanation": row[6].split(" | "),
            "timestamp": row[7]
        })

    return results
if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")