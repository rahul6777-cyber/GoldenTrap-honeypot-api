from fastapi import FastAPI, Depends, Body
from typing import Optional
from detector import detect_scam
from responder import generate_reply
from extractor import extract_intel
from security import verify_api_key

app = FastAPI(title="Agentic Scam Honeypot API")


# --------------------------------------------------
# ✅ ROOT HEALTH CHECK
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "API running",
        "service": "Agentic Scam Honeypot API"
    }


# --------------------------------------------------
# ✅ TEST ENDPOINT (HACKATHON VALIDATION)
# --------------------------------------------------
@app.post("/honeypot/test")
def honeypot_test(
    payload: Optional[dict] = Body(None),
    api_key: str = Depends(verify_api_key)
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
# 🕵️ REAL HONEYPOT ENDPOINT
# --------------------------------------------------
@app.post("/webhook/message")
def message(data: dict, api_key: str = Depends(verify_api_key)):
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
