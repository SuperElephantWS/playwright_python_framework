import pytest
from playwright.sync_api import Page, expect
import time

# Matches what you set in test_signup_and_save_session
EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"

def test_mission_06(page: Page):
    # Navigate directly to a page that requires you to be logged in
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")
    time.sleep(3)

    # click button
    page.get_by_role("button", name="Click to Complete").click()
    time.sleep(3)

    # check for confirmation message
    expect(page.locator("#button-result strong"))
    time.sleep(5)