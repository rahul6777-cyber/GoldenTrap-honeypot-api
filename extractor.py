# extractor.py
import re

URL_REGEX = r"(https?://[^\s]+)"
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
PHONE_REGEX = r"\b\d{10}\b"
UPI_REGEX = r"\b[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}\b"

def extract_intel(text: str):
    return {
        "urls": re.findall(URL_REGEX, text),
        "emails": re.findall(EMAIL_REGEX, text),
        "phone_numbers": re.findall(PHONE_REGEX, text),
        "upi_ids": re.findall(UPI_REGEX, text)
    }
