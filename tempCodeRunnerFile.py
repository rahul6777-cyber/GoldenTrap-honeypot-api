# security.py

import os
from fastapi import Header, HTTPException, status
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "BROCODE123")  # fallback for demo


def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key missing"
        )

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return x_api_key