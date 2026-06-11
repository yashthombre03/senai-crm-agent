def classify_email(text):

    text = text.lower()

    if any(
        word in text
        for word in [
            "refund",
            "complaint",
            "unhappy"
        ]
    ):
        return "Complaint"

    if any(
        word in text
        for word in [
            "price",
            "discount",
            "billing"
        ]
    ):
        return "Billing"

    if any(
        word in text
        for word in [
            "breach",
            "ransomware",
            "attack"
        ]
    ):
        return "Security"

    if any(
        word in text
        for word in [
            "feature",
            "enhancement"
        ]
    ):
        return "Feature Request"

    return "General Inquiry"