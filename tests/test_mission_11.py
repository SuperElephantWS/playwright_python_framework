from playwright.sync_api import expect


EXPECTED_TITLE = (
    "Playwright, Selenium & Cypress Practice | "
    "Interactive Automation Testing Playground"
)


def test_mission_11(page):

    page.goto(
        "https://faruk-hasan.com/automation/"
        "playwright-selenium-cypress-practice.html",
        wait_until="domcontentloaded"
    )

    expect(page).to_have_title(EXPECTED_TITLE)

    # Find the row we need...
    veggie_row = page.locator("tr").filter(
        has_text="Veggie"
    ).filter(
        has_text="Medium"
    )

    # Click Process butto
    veggie_row.get_by_role("button", name="Process").click()

    # Verify that sucker
    result = page.locator("#table-result")

    expect(result).to_have_text(
        "Success! Mission 11 complete. "
        "You processed the correct order (#1002 - Veggie)."
    )