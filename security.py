import os
from fastapi import Header, HTTPException, status

API_KEY = os.getenv("API_KEY", "BROCODE123")


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


def verify_api_key_optional(x_api_key: str = Header(None)):
    # GUVI tester may omit headers
    if x_api_key is None:
        return "guvi-test"
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return x_api_key
