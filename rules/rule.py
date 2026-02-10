import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "data.csv"
print(DATA_PATH.exists())


suggestion = []

def run_rules(text):
    text = text.lower()
    suggestion = []

    if "never" in text or "always" in text:
        suggestion.append("overgeneralization")

    if "they think" in text or "everyone thinks" in text:
        suggestion.append("mind_reading")

    if "should" in text or "must" in text:
        suggestion.append("should_statements")

    if ("i will" in text or "i am") and "fail" in text:
        suggestion.append("fortune_telling")

    if "ruined" in text or "worst" in text or "destroy" in text:
        suggestion.append("catastrophizing")

    if "i feel" in text and ("fail" in text or "failure" in text or "loser" in text):
        suggestion.append("emotional_reasoning")

    return suggestion