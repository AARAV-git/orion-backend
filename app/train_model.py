import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# 1. Load Data
df = pd.read_csv(r'C:\Users\sunny\Desktop\CodeAThon\orion-backend\data\synthetic_medical_triage.csv')

# 2. Map Dataset Triage Levels (0-3) to Your Backend Urgency Scores (1-5)
# Dataset: 3=Critical, 2=Emergency, 1=Urgent, 0=Non-Urgent
# Backend: 1=Critical ... 5=Non-Urgent
label_mapping = {
    3: 1,  # Critical
    2: 2,  # Emergency
    1: 3,  # Urgent
    0: 5   # Non-Urgent
}
df['urgency_score'] = df['triage_level'].map(label_mapping)

# 3. Select Features (Only those we can easily extract from text input)
# We exclude 'arrival_mode' and history counts to simplify the demo input
features = [
    'age',
    'heart_rate',
    'systolic_blood_pressure',
    'oxygen_saturation',
    'body_temperature',
    'pain_level'
]

X = df[features]
y = df['urgency_score']

# 4. Train Model
print("Training Random Forest Model...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# 5. Validate
preds = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, preds):.2f}")
print("\nClassification Report:\n", classification_report(y_test, preds))

# 6. Save Model
with open("app/ai/triage_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved to app/ai/triage_model.pkl")
