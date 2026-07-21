import pytest
from playwright.sync_api import Page, expect
import time

# Matches what you set in test_signup_and_save_session
EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"
def test_mission_03(page: Page):
    # Navigate directly to a page that requires you to be logged in
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")
    # Find the payment method radio buttons
    # credit_card = page.locator("#credit")
    # paypal = page.locator("#paypal")
    # bitcoin = page.locator("#bitcoin")
    # time.sleep(3)
    # Click the "Confirm Payment" button



    page.get_by_text("Credit Card").click()
    page.get_by_role("button", name="Confirm Payment").click()
    # payment_button = page.get_by_role("button", name="Confirm Payment")
    # payment_button.click()
    # Check for verfication message
    expect(page.locator("#radio-result strong")).to_have_text("credit")
    time.sleep(5)



    page.get_by_text("PayPal").click()
    page.get_by_role("button", name="Confirm Payment").click()
    # payment_button = page.get_by_role("button", name="Confirm Payment")
    # payment_button.click()
    # Check for verfication message
    expect(page.locator("#radio-result strong")).to_have_text("paypal")
    time.sleep(5)


    page.get_by_text("Bitcoin").click()
    page.get_by_role("button", name="Confirm Payment").click()
    # payment_button = page.get_by_role("button", name="Confirm Payment")
    # payment_button.click()
    # Check for verfication message
    expect(page.locator("#radio-result strong")).to_have_text("bitcoin")
    time.sleep(5)