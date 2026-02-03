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
async def honeypot_test(request: Request):
    return {
        "status": "success",
        "message": "Honeypot endpoint reachable",
        "agent": "active",
        "capabilities": [
            "scam_detection",
            "auto_response",
            "intelligence_extraction"
        ],
        "version": "1.0.0"
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
