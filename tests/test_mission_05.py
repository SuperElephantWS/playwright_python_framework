import pytest
from playwright.sync_api import Page, expect
import time

from pytest_playwright.pytest_playwright import page

# Matches what you set in test_signup_and_save_session
EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"

def test_draggable(page: Page):
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")

    # expect(page).to_have_title(EXPECTED_TITLE)
    time.sleep(3)  # Wait for the page to load

    # Identify the draggable item
    draggable_box = page.locator("#draggable")
    drop_container_box = page.locator("#drop-container")
    time.sleep(3)
    draggable_box.hover();
    page.mouse.down();
    drop_container_box.hover();
    page.mouse.up();
    time.sleep(5)
    drag_result = page.locator("strong")
    expect(drag_result).to_contain_text("Success!")
    time.sleep(5)  # Wait for the result to be visible