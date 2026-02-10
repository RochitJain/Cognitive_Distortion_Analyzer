DISTORTION_DEFINITIONS = {
    "overgeneralization": "Drawing a broad conclusion from a single event.",
    "catastrophizing": "Assuming the worst possible outcome without sufficient evidence.",
    "mind_reading": "Assuming you know what others think without evidence.",
    "fortune_telling": "Predicting the future as if it is certain.",
    "emotional_reasoning": "Treating feelings as facts.",
    "personalization": "Taking responsibility for events outside your control.",
    "should_statements": "Using rigid rules about how things must be.",
    "all_or_nothing_thinking": "Seeing situations in black-and-white terms.",
    "none": "No cognitive distortion detected."
}

def extract_evidence(text, label):
    text = text.lower()

    if label == "overgeneralization":
        for w in ["always", "never", "everything", "nothing"]:
            if w in text:
                return w

    if label == "catastrophizing":
        for w in ["ruined", "destroy", "life is over", "fall apart"]:
            if w in text:
                return w

    if label == "mind_reading":
        for w in ["they think", "everyone thinks", "must think"]:
            if w in text:
                return w

    if label == "fortune_telling":
        for w in ["will fail", "going to fail", "will never"]:
            if w in text:
                return w

    if label == "should_statements":
        for w in ["should", "must"]:
            if w in text:
                return w

    return "implicit assumption"

def generate_explanation(text, final_label):
    definition = DISTORTION_DEFINITIONS[final_label]
    evidence = extract_evidence(text, final_label)

    if final_label == "none":
        return "The statement reflects balanced or adaptive thinking."

    return (
        f"Detected distortion: {final_label}. "
        f"Evidence: '{evidence}'. "
        f"This fits because it involves {definition.lower()}"
    )