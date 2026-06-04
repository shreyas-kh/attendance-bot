import requests
import os

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSewV0cL15tjhXHsP82N-gpqzCMeT-QyCiLq43pK5v4wXK-d6g/formResponse"

data = {
    "entry.711263147":   os.environ["FORM_NAME"],
    "entry.1594989021":  os.environ["FORM_TOKEN"],
    "entry.1107370927":  "",   # Any comments — left empty
}

response = requests.post(FORM_URL, data=data)

if response.status_code == 200:
    print("✅ Punch-out submitted successfully!")
else:
    print(f"❌ Punch-out failed with status code: {response.status_code}")