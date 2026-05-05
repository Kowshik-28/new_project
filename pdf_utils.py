import pdfplumber
import re

def extract_text(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_license_plate(text):
    match = re.search(r'[A-Z]{2}-\d{3}-[A-Z]', text)
    return match.group() if match else None

def extract_driver_name(text):
    match = re.search(r'Driver:\s*(\w+\s\w+)', text)
    return match.group(1) if match else None

def extract_packing_slip(text):
    match = re.search(r'Slip\s*No[:\-]?\s*(\d+)', text)
    return match.group(1) if match else None