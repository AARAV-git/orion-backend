from pydantic import BaseModel, Field
from typing import Optional

class PatientSchema(BaseModel):
    name: str = Field(..., example="Rahul Sharma")
    pain_score: int
    duration_hours: int
    age: Optional[int] = None   # auto-fill
    spo2: int
    temperature: float
    chronic_disease: int
    red_flag: int
    verbal_problem: Optional[str] = None   # auto-fill
    doctor_email: Optional[str] = None
    emergency: Optional[bool] = False
