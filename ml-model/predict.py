import sys
import joblib

# Correct paths
model = joblib.load("ml-model/model.pkl")
vectorizer = joblib.load("ml-model/vectorizer.pkl")

log_text = sys.stdin.read().strip()

if not log_text:
    print("No log input received")
    exit()

X = vectorizer.transform([log_text])
prob = model.predict_proba(X)[0][1]

print(prob)
