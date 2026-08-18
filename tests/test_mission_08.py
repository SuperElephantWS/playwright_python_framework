import pytest
from playwright.sync_api import Page, expect
import time

# Matches what you set in test_signup_and_save_session
EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"

def test_mission_08(page: Page):
    # Navigate directly to a page that requires you to be logged in
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")
    time.sleep(3)

    # click button
    page.get_by_role("button", name="Toggle Mission 7").click()

    #check for alert message
    expect(page.locator("#hide-result strong")).to_have_text("Mission 7 is now hidden!")
    time.sleep(3)

    #refresh page
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")
    time.sleep(5)