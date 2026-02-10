import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from reconcile.reconcile import reconcile_prediction
from rules.rule import run_rules
from explains.explain import generate_explanation

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "data.csv"
print(DATA_PATH.exists())

data = pd.read_csv(DATA_PATH)

x = data["text"]
y = data["distortion_type"]

vectoriser = TfidfVectorizer(
    lowercase= True
)

X = vectoriser.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1
)

X_train = vectoriser.fit_transform(x_train)
X_test = vectoriser.transform(x_test)

model = LogisticRegression()
model.fit(X_train,y_train)

# predictions = model.predict(X_test)

proba = model.predict_proba(X_test)
predictions = model.predict(X_test)

final_predictions = []

for i, text in enumerate(x_test):
    ml_label = predictions[i]
    ml_confidence = max(proba[i])

    rule_suggestions = run_rules(text)

    final_label = reconcile_prediction(
        text,
        ml_label,
        ml_confidence,
        rule_suggestions
    )
    explanation = generate_explanation(text, final_label)

    final_predictions.append(final_label)
    print("TEXT:", text)
    print("PREDICTION:", final_label)
    print("EXPLANATION:", explanation)
    print("-----")

print(classification_report(y_test, final_predictions))