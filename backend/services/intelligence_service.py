#SPAM Detection
SPAM_KEYWORDS = [
    "seo",
    "backlinks",
    "bitcoin",
    "crypto",
    "prince",
    "million dollars",
    "click here",
    "marketing package"
]

def detect_spam(text):

    text = text.lower()

    for keyword in SPAM_KEYWORDS:

        if keyword in text:
            return True

    return False

#Security Detection
SECURITY_KEYWORDS = [
    "breach",
    "hacked",
    "ransomware",
    "compromised",
    "attack",
    "security incident",
    "credential"
]

def detect_security_issue(text):

    text = text.lower()

    for keyword in SECURITY_KEYWORDS:

        if keyword in text:
            return True

    return False

#Internal Email detection
def is_internal_email(email):

    INTERNAL_DOMAINS = [
        "@internal.com",
        "@mycompany.com"
    ]

    email = email.lower()

    return any(
        email.endswith(domain)
        for domain in INTERNAL_DOMAINS
    )

#Urgency Detection
URGENT_KEYWORDS = [
    "urgent",
    "critical",
    "asap",
    "immediately",
    "production down",
    "legal",
    "lawsuit",
    "cease and desist"
]

def detect_urgency(text):

    text = text.lower()

    for keyword in URGENT_KEYWORDS:

        if keyword in text:
            return "High"

    return "Normal"

#Intelligence Summary Function
def analyze_email(
    sender,
    body
):

    return {

        "is_spam": detect_spam(body),

        "security_alert":
            detect_security_issue(body),

        "internal_email":
            is_internal_email(sender),

        "urgency":
            detect_urgency(body)
    }