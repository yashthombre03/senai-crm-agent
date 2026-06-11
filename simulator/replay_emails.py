import json
import requests

API_URL = "http://127.0.0.1:8000/api/ingest"

with open(
    "dataset/email-data-advanced.json",
    "r",
    encoding="utf-8"
) as file:

    emails = json.load(file)

print(f"Loaded {len(emails)} emails")

for email in emails:


    response = requests.post(
        API_URL,
        json=email
    )

    print(
        email["message_id"],
        response.status_code
    )

    try:
        print(response.json())

    except:
        print(response.text)

    print("-" * 40)