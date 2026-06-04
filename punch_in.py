import requests
import os

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdB3k3SDcnla5sSAHdstvUEokxL66c_8cYSZKVp0BZQDc51lA/formResponse"

data = {
    "entry.1375000112": os.environ["FORM_NAME"],
    "entry.1720683654": os.environ["FORM_TOKEN"],
    "entry.1365288235": os.environ["FORM_MESSAGE"],
}

response = requests.post(FORM_URL, data=data)

if response.status_code == 200:
    print("✅ Punch-in submitted successfully!")
else:
    print(f"❌ Punch-in failed with status code: {response.status_code}")