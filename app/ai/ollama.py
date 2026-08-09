# app/ai/ollama.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_reasoning(patient, score, label, summary):

    prompt = f"""
You are an emergency triage doctor.

Patient Summary:
{summary}

Patient Complaint:
"{patient.get('verbal_problem', 'Not provided')}"

Urgency Score: {score}/10 -> {label}

Write EXACTLY 5 short bullet points explaining the medical reasoning.
Each bullet must be ONE complete sentence, under 15 words.
Do NOT write any introduction or conclusion.
"""

    res = requests.post(OLLAMA_URL, json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 140
        }
    })

    return res.json()["response"]
