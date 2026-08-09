from app.automation.alerts import send_emergency_alert, send_patient_notification


def execute_actions(patient_data, triage_result):

    score = triage_result["urgency_score"]
    label = triage_result["urgency_level"]
    summary = triage_result["clinical_summary"]

    # ---------------- DOCTOR ALERT (OPTIONAL) ----------------
    doctor_email = patient_data.get("doctor_email")

    if doctor_email and score >= 9:
        send_emergency_alert(
            patient_data,
            score,
            label,
            summary,
            doctor_email
        )

    # ---------------- PATIENT EMAIL (OPTIONAL) ----------------
    patient_email = patient_data.get("email")

    if patient_email:
        send_patient_notification(
            patient_data,
            score,
            label,
            summary,
            patient_email
        )

    return True
