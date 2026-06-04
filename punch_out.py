import os
import json
import sys
from playwright.sync_api import sync_playwright

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSewV0cL15tjhXHsP82N-gpqzCMeT-QyCiLq43pK5v4wXK-d6g/viewform"

try:
    auth_state = json.loads(os.environ["GOOGLE_AUTH_JSON"])
except KeyError:
    print("❌ Missing GOOGLE_AUTH_JSON secret")
    sys.exit(1)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=auth_state)
        page = context.new_page()
        
        page.goto(FORM_URL)
        page.wait_for_load_state("networkidle")
        
        page.locator('div[role="checkbox"]').first.click()
        
        text_inputs = page.locator('input[type="text"], textarea')
        
        text_inputs.nth(0).fill(os.environ["FORM_NAME"])
        text_inputs.nth(1).fill(os.environ["FORM_TOKEN"])
        
        page.locator('div[role="button"]:has-text("Submit")').click()
        page.wait_for_timeout(3000) 
        
        print("✅ Punch-out submitted successfully via Playwright!")
        browser.close()
except Exception as e:
    print(f"❌ Automation failed! Error: {e}")
    sys.exit(1)