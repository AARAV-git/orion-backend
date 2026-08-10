from app.automation.alerts import send_emergency_alert, send_patient_notification


def execute_actions(patient_data, triage_result):

    score = triage_result["urgency_score"]
    label = triage_result["urgency_level"]
    summary = triage_result["clinical_summary"]

    target_email = patient_data.get("doctor_email") or patient_data.get("email")

    if target_email:
        # Trigger Doctor Emergency Alert if score >= 7 (High / Critical Priority) or emergency flag
        if score >= 7.0 or patient_data.get("emergency"):
            send_emergency_alert(
                patient_data,
                score,
                label,
                summary,
                target_email
            )

        # Always trigger Patient Medical Status Update if an email is provided
        send_patient_notification(
            patient_data,
            score,
            label,
            summary,
            target_email
        )

    return True
