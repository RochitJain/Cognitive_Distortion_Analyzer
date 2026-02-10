def has_catastrophic_language(text):
    catastrophic_words = [
        "ruined",
        "destroy",
        "life is over",
        "everything will fall apart",
        "end of my career"
    ]
    return any(word in text.lower() for word in catastrophic_words)


def has_corrective_language(text):
    corrective_markers = [
        "but i learned",
        "but i can",
        "next time",
        "i will improve",
        "i can try again"
    ]
    return any(marker in text.lower() for marker in corrective_markers)


def reconcile_prediction(text, ml_label, ml_confidence, rule_suggestions):

    # Rule 1: Catastrophizing override
    if (
        "catastrophizing" in rule_suggestions
        and has_catastrophic_language(text)
        and ml_confidence < 0.7
    ):
        return "catastrophizing"

    # Rule 2: None override
    if (
        ml_label != "none"
        and has_corrective_language(text)
    ):
        return "none"

    return ml_label