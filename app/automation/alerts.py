import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_SENDER = "sunnypathak979@gmail.com"
EMAIL_PASSWORD = "awre kxgo bnfr xtjr"   # Use App Password


# ---------------- DOCTOR EMERGENCY ALERT ----------------

def send_emergency_alert(patient, score, label, summary, receiver_email):

    subject = "🚨 CRITICAL EMERGENCY ALERT"

    body = f"""
CRITICAL TRIAGE ALERT

Patient: {patient.get('name','Patient')}

Urgency Score: {score}/10
Status: {label}

Clinical Summary:
{summary}

Immediate medical attention is required.
"""

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("📧 Emergency email alert sent successfully.")

    except Exception as e:
        print("❌ Emergency email failed:", e)


# ---------------- PATIENT NOTIFICATION ----------------

def send_patient_notification(patient, score, label, summary, receiver_email):

    subject = "ORION Health — Medical Status Update"

    if score >= 9:
        advice = "This is a medical emergency. Please go to the nearest emergency department immediately."
    elif score >= 7:
        advice = "Your condition requires urgent medical attention. Please visit the hospital as soon as possible."
    elif score >= 5:
        advice = "Your symptoms require a doctor's consultation. Please schedule a visit."
    else:
        advice = "Your symptoms appear mild. Rest and home care are advised."

    body = f"""
Dear {patient.get('name','Patient')},

Here is your medical status update:

Urgency Score: {score}/10
Status: {label}

Clinical Summary:
{summary}

Medical Advice:
{advice}

⚠️ This is an AI-assisted triage result and does not replace professional medical advice.

ORION-Health Team
"""

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("📧 Patient email notification sent successfully.")

    except Exception as e:
        print("❌ Patient email failed:", e)
