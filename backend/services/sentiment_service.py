
NEGATIVE_WORDS = [
    "angry",
    "refund",
    "unhappy",
    "cancel",
    "broken",
    "crash",
    "error",
    "urgent",
    "threat",
    "lawsuit",
    "legal"
]

POSITIVE_WORDS = [
    "love",
    "great",
    "excellent",
    "thanks",
    "happy",
    "amazing"
]

def calculate_sentiment(
    text
):

    text = text.lower()

    score = 0

    for word in POSITIVE_WORDS:

        if word in text:
            score += 1

    for word in NEGATIVE_WORDS:

        if word in text:
            score -= 1

    return score