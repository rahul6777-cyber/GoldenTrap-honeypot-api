from fastapi import FastAPI, Depends, Body
from typing import Any, Optional

from detector import detect_scam
from responder import generate_reply
from extractor import extract_intel
from security import verify_api_key, verify_api_key_optional

app = FastAPI(title="Agentic Scam Honeypot API")


# --------------------------------------------------
# ✅ ROOT HEALTH CHECK (OPTIONAL)
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "API running",
        "service": "Agentic Scam Honeypot API"
    }


# --------------------------------------------------
# ✅ GUVI / HACKATHON VALIDATION ENDPOINT
# (Relaxed: accepts any body, optional API key)
# --------------------------------------------------
@app.post("/honeypot/test")
def honeypot_test(
    payload: Any = Body(default=None),
    api_key: str = Depends(verify_api_key_optional)
):
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
# 🕵️ REAL HONEYPOT AGENT ENDPOINT (STRICT & SECURE)
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
