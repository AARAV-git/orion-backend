from pydantic import BaseModel
from typing import Optional

class PreRegisterSchema(BaseModel):
    hospital_name: Optional[str] = None
    patient_name: str
    age: int
    problem: str
    email: Optional[str] = None
