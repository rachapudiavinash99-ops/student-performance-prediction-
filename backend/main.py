from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title="Student Performance API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentData(BaseModel):
    rollNo: str
    branch: str
    semester: str
    cgpa: float
    activeBacklogs: int
    attendance: float

class SemData(BaseModel):
    studentId: str
    midSemMarks: float
    attendance: float
    assignments: int

@app.get("/")
def read_root():
    return {"message": "Welcome to Student Performance Prediction API"}

@app.post("/api/predictions/risk")
def predict_risk(data: StudentData):
    # Mock logic matching BTech frontend
    score = (data.cgpa * 10) * 0.4 + data.attendance * 0.4 - (data.activeBacklogs * 10)
    prob = max(0, min(100, 100 - score + 20))
    risk = "Low"
    if prob > 70: risk = "High"
    elif prob > 40: risk = "Medium"
    
    return {"risk": risk, "probability": round(prob)}

@app.post("/api/predictions/semester")
def predict_sem(data: SemData):
    score = (data.midSemMarks * 0.4) + (data.attendance * 0.4) + (data.assignments * 2)
    grade = 'C'
    sgpa = 6.5
    if score > 85: grade, sgpa = 'O', 9.5
    elif score > 75: grade, sgpa = 'A+', 8.5
    elif score > 65: grade, sgpa = 'A', 7.5
    elif score > 55: grade, sgpa = 'B+', 6.5
    else: grade, sgpa = 'F', 4.0
    return {"grade": grade, "sgpa": sgpa}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
