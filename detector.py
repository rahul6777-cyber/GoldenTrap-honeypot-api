# detector.py

SCAM_KEYWORDS = [
    "blocked",
    "suspended",
    "urgent",
    "immediately",
    "verify",
    "kyc",
    "refund",
    "upi",
    "account",
    "click",
    "link",
    "payment"
]

def detect_scam(message: str):
    message_lower = message.lower()
    matched = []

    for word in SCAM_KEYWORDS:
        if word in message_lower:
            matched.append(word)

    scam_detected = len(matched) >= 2

    return {
        "scam_detected": scam_detected,
        "matched_keywords": matched,
        "risk_score": len(matched)
    }