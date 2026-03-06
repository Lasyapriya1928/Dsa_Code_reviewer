import sqlite3
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "submissions.db")

print("USING DATABASE AT:", DB_PATH)


# -----------------------------
# Initialize DB
# -----------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            hashed_password TEXT
        )
    """)

    # Create submissions table
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

    # Convert UTC → IST
    timestamp = (datetime.utcnow() + timedelta(hours=5, minutes=30)).isoformat()

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
        timestamp
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


# -----------------------------
# User Functions
# -----------------------------
def create_user(username, email, hashed_password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, email, hashed_password)
        VALUES (?, ?, ?)
    """, (username, email, hashed_password))

    conn.commit()
    conn.close()


def get_user_by_username(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, email, hashed_password
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()
    conn.close()

    if user:
        return {
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "hashed_password": user[3]
        }

    return None


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")