import pytest
from playwright.sync_api import Page, expect

EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"


def test_mission_07(page: Page):
    # Navigate to the page
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")

    # Did the page load?
    expect(page).to_have_title(EXPECTED_TITLE)

    # Search elements
    search_input = page.locator("#search-input")
    search_button = page.get_by_role("button", name="Search")
    search_result = page.locator("#search-result")
    search_term = page.locator("#search-result strong")

    # Search for a pizza
    pizza = "pepperoni"
    search_input.fill(pizza)
    search_button.click()

    # Verify results
    expect(search_input).to_have_value(pizza)
    expect(search_result).to_contain_text("You searched for:")
    expect(search_term).to_have_text(pizza)