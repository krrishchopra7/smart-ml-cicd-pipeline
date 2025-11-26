import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

log_dir = "logs"

logs = []
labels = []

for file in os.listdir(log_dir):
    with open(f"{log_dir}/{file}", "r") as f:
        content = f.read()
        logs.append(content)
        labels.append(0 if "success" in file else 1)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(logs)

model = RandomForestClassifier()
model.fit(X, labels)

joblib.dump(model, "ml-model/model.pkl")
joblib.dump(vectorizer, "ml-model/vectorizer.pkl")

print("Model trained successfully!")
