from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer

from backend.analyzer import analyze_code
from backend.database import (
    get_all_submissions,
    create_user,
    get_user_by_username,
    save_submission   # ✅ ADD THIS
)

app = FastAPI(title="AlgoScope API")

# -----------------------------
# Security Settings
# -----------------------------
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(credentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# -----------------------------
# Request Models
# -----------------------------
class CodeRequest(BaseModel):
    code: str
    problem_name: str
    save: bool = False


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def root():
    return {"message": "AlgoScope API running"}


@app.post("/register")
def register(request: RegisterRequest):
    existing_user = get_user_by_username(request.username)

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = pwd_context.hash(request.password)
    create_user(request.username, request.email, hashed_password)

    return {"message": "User registered successfully"}


@app.post("/login")
def login(request: LoginRequest):

    user = get_user_by_username(request.username)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not pwd_context.verify(request.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(
        data={"sub": user["username"]}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.post("/analyze")
def analyze(
    request: CodeRequest,
    current_user: str = Depends(get_current_user)
):
    result = analyze_code(
        request.code,
        request.problem_name
    )

    # ✅ Save only when Save button is clicked
    if request.save and not result.get("error"):
        save_submission(
            request.problem_name,
            result["predicted_efficiency"],   # correct order
            result["predicted_pattern"],      # correct order
            result["explanation"],            # explanation list
            request.code                     # code LAST
        )

    return result
@app.get("/history")
def history(current_user: str = Depends(get_current_user)):
    return get_all_submissions()


# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------
# ANALYTICS ROUTE (SAFE VERSION)
# --------------------------------------

import sqlite3
from collections import Counter

@app.get("/analytics")
def get_analytics():

    conn = sqlite3.connect("backend/submissions.db")
    cursor = conn.cursor()

    cursor.execute("SELECT problem_name, predicted_pattern, predicted_efficiency FROM submissions")
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        return {
            "total_submissions": 0,
            "unique_problems": 0,
            "pattern_distribution": {},
            "efficiency_distribution": {}
        }

    total_submissions = len(rows)
    unique_problems = len(set(r[0] for r in rows))

    pattern_counts = Counter(r[1] for r in rows)
    efficiency_counts = Counter(r[2] for r in rows)

    return {
        "total_submissions": total_submissions,
        "unique_problems": unique_problems,
        "pattern_distribution": dict(pattern_counts),
        "efficiency_distribution": dict(efficiency_counts)
    }