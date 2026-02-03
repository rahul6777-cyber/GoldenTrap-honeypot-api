# responder.py

def generate_reply(analysis: dict):
    if not analysis["scam_detected"]:
        return "Thank you for your message. We will get back to you shortly."

    replies = [
        "I am not sure what this is about. Can you explain?",
        "Why is my account blocked? I did not do anything.",
        "Can you share official details or reference number?",
        "I need time to check this. Please wait."
    ]

    # simple rotation based on risk score
    index = analysis["risk_score"] % len(replies)
    return replies[index]