import time

from playwright.sync_api import expect


EXPECTED_TITLE = (
    "Playwright, Selenium & Cypress Practice | "
    "Interactive Automation Testing Playground"
)


def test_mission_10(page):

    page.goto(
        "https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html",
        wait_until="domcontentloaded"
    )

    expect(page).to_have_title(EXPECTED_TITLE)

    tooltip_box = page.locator("#tooltip-trigger")
    tooltip_box.hover()
    time.sleep(3)  # Wait for the tooltip to appear


    expect(page.locator("#tooltip-box")).to_have_text(
        "Tooltip is visible only when you hover!")

    time.sleep(3)