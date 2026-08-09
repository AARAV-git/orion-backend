import os
import random
import pandas as pd
from faker import Faker

fake = Faker()

NUM_SAMPLES = 100000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "sample_patients.csv")


def calculate_urgency(p):
    """
    Medical rule-based urgency scoring
    1 → Non-urgent
    2 → Low
    3 → Moderate
    4 → High
    5 → Critical
    """

    # Critical
    if p["unconscious"] == 1 or p["oxygen_level"] < 85:
        return 5

    # High
    if p["chest_pain"] == 1 and p["breathing_difficulty"] == 1:
        return 4

    if p["temperature"] > 102 and p["heart_rate"] > 120:
        return 4

    # Moderate
    if p["heart_rate"] > 110 or p["systolic_bp"] > 160:
        return 3

    # Low
    if p["temperature"] > 100:
        return 2

    # Non urgent
    return 1


def generate_patient():
    p = {
        "age": random.randint(1, 90),
        "heart_rate": random.randint(60, 150),
        "systolic_bp": random.randint(90, 190),
        "diastolic_bp": random.randint(60, 120),
        "temperature": round(random.uniform(97.0, 104.0), 1),
        "oxygen_level": random.randint(80, 100),
        "chest_pain": random.choice([0, 1]),
        "breathing_difficulty": random.choice([0, 1]),
        "unconscious": random.choice([0, 1])
    }

    p["urgency"] = calculate_urgency(p)
    return p


def main():
    print("📌 Generating dataset...")
    print("📂 Saving to:", OUTPUT_PATH)

    data = [generate_patient() for _ in range(NUM_SAMPLES)]
    df = pd.DataFrame(data)

    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Dataset generated successfully!")


if __name__ == "__main__":
    main()
