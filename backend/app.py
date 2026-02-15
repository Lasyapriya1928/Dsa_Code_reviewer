from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.analyzer import analyze_code
from backend.database import get_all_submissions


app = FastAPI(title="AlgoScope API")

class CodeRequest(BaseModel):
    code: str
    problem_name: str

@app.get("/")
def root():
    return {"message": "AlgoScope API running"}

@app.post("/analyze")
def analyze(request: CodeRequest):
    return analyze_code(request.code, request.problem_name)

@app.get("/history")
def history():
    return get_all_submissions()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)