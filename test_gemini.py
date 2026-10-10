import os
import requests
import json

api_key = os.environ.get("GEMINI_API_KEY", "")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [{"parts": [{"text": 'Deconstruct the product "Davidoff Espresso 57 100g" into physical packaging materials and ingredients. Return valid JSON only.'}]}],
    "generationConfig": {"temperature": 0.1, "response_mime_type": "application/json"}
}

if api_key:
    r = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
    print("Status:", r.status_code)
    print("Response text:\n", r.text[:600])
else:
    print("No GEMINI_API_KEY environment variable provided.")
