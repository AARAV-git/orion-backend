# app/test_full_pipeline.py

from app.ai_pipeline import run_triage_pipeline

sample = {
    "pain_score": 10,
    "duration_hours": 1,
    "age": 72,
    "spo2": 84,
    "temperature": 40.3,
    "chronic_disease": 1,
    "red_flag": 1,
    "verbal_problem": "Severe chest pain, unconsciousness, and breathing difficulty"
}


result = run_triage_pipeline(sample)

print("\n", "="*60)
print("URGENCY SCORE:", result["urgency_score"])
print("URGENCY LEVEL:", result["urgency_level"])
print("\nSUMMARY:", result["clinical_summary"])
print("\nAI EXPLANATION:\n", result["explanation"])
print("="*60)
