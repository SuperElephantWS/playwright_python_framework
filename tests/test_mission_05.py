import pytest
from playwright.sync_api import Page, expect
import time

from pytest_playwright.pytest_playwright import page

# Matches what you set in test_signup_and_save_session
EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"

def test_draggable(page: Page):
    page.goto("https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html")

    def drag_element(page, source_selector, target_selector):
        page.evaluate(
            """
            ({ sourceSelector, targetSelector }) => {
                const source = document.querySelector(sourceSelector);
                const target = document.querySelector(targetSelector);

                const dataTransfer = new DataTransfer();

                dataTransfer.setData("text/plain", source.id);

                source.dispatchEvent(
                    new DragEvent("dragstart", {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer
                    })
                );

                target.dispatchEvent(
                    new DragEvent("dragover", {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer
                    })
                );

                target.dispatchEvent(
                    new DragEvent("drop", {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer
                    })
                );

                source.dispatchEvent(
                    new DragEvent("dragend", {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer
                    })
                );
            }
            """,
            {
            "sourceSelector": source_selector,
            "targetSelector": target_selector
            }
    )

    # expect(page).to_have_title(EXPECTED_TITLE)
    time.sleep(3)  # Wait for the page to load

    # Identify the draggable item
    time.sleep(3)
    drag_element(page, "#draggable", "#drop-container")
    time.sleep(5)
    drag_result = page.locator("#drag-result")
    expect(drag_result).to_contain_text("Success!")
    expect(drag_result).to_contain_text("Item dropped correctly!")
    time.sleep(5)  # Wait for the result to be visible