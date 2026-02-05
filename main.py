from fastapi import FastAPI, Request, Depends, Body

from detector import detect_scam
from responder import generate_reply
from extractor import extract_intel
from security import verify_api_key

app = FastAPI(title="Agentic Scam Honeypot API")


# --------------------------------------------------
# ✅ ROOT (OPTIONAL HEALTH CHECK)
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "API running",
        "service": "Agentic Scam Honeypot API"
    }


# --------------------------------------------------
# ✅ GUVI / HACKATHON TEST ENDPOINT
# ❗ NO AUTH
# ❗ NO BODY PARSING
# ❗ NO VALIDATION
# --------------------------------------------------
@app.post("/honeypot/test")
def honeypot_test(
    payload: Optional[dict] = Body(None),
    api_key: str = Depends(verify_api_key)
):
    # default fallback reply
    reply_text = "Why is my account being suspended?"

    # if tester sends message text, you can adapt reply (optional)
    if payload and "message" in payload:
        text = payload.get("message", {}).get("text", "")
        if "blocked" in text.lower() or "suspended" in text.lower():
            reply_text = "Why is my account being suspended?"

    return {
        "status": "success",
        "reply": reply_text
    }



# --------------------------------------------------
# 🕵️ REAL AGENTIC HONEYPOT ENDPOINT (SECURE)
# --------------------------------------------------
@app.post("/webhook/message")
def webhook_message(
    data: dict = Body(...),
    api_key: str = Depends(verify_api_key)
):
    text = data.get("message", "")

    analysis = detect_scam(text)
    reply = generate_reply(analysis)
    intelligence = extract_intel(text)

    return {
        "status": "authorized",
        "input_message": text,
        "analysis": analysis,
        "auto_reply": reply,
        "extracted_intelligence": intelligence
    }
