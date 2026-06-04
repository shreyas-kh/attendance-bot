import os
import json
import sys
from playwright.sync_api import sync_playwright

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdB3k3SDcnla5sSAHdstvUEokxL66c_8cYSZKVp0BZQDc51lA/viewform"

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
        
        page.locator('[name="entry.1375000112"]').fill(os.environ["FORM_NAME"])
        page.locator('[name="entry.1720683654"]').fill(os.environ["FORM_TOKEN"])
        page.locator('[name="entry.1365288235"]').fill(os.environ["FORM_MESSAGE"])
        
        page.locator('div[role="button"]:has-text("Submit")').click()
        page.wait_for_timeout(3000) 
        
        print("✅ Punch-in submitted successfully via Playwright!")
        browser.close()
except Exception as e:
    print(f"❌ Automation failed! Error: {e}")
    sys.exit(1)