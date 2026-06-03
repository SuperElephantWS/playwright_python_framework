import pytest
from playwright.sync_api import Page, expect
import time

# Matches what you set in test_signup_and_save_session
EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"

def test_mission_01(page: Page):
    # Navigate directly to a page that requires you to be logged in
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")
    pizza_options = page.locator("#pizza-size option")
    pizza_list = []
    for option in pizza_options.all():
        size = option.get_attribute("value")
        if size and size != "-- Select Size--":
            pizza_list.append(size)
    print(f"\n[TEST] Available pizza size options: {pizza_list}")
    for size in pizza_list:
        print(f"\n[TEST] Pizza size option: {size}")
        print(size)
        pizza_dropdown = page.locator("#pizza-size")
        # Open/select by value
        pizza_dropdown.select_option(value=size.lower())
        # Wait and assert the underlying value is set
        pizza_button = page.get_by_role("button", name="Confirm Selection")
        pizza_button.click()
        expect(pizza_dropdown).to_have_value(size.lower())
        # Optionally assert the displayed option text
        expect(page.locator("#dropdown-result strong")).to_have_text(size)
        time.sleep(1)