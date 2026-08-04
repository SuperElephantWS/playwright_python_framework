from playwright.sync_api import expect


EXPECTED_TITLE = (
    "Playwright, Selenium & Cypress Practice | "
    "Interactive Automation Testing Playground"
)


def test_mission_09(page):

    page.goto(
        "https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html",
        wait_until="domcontentloaded"
    )

    expect(page).to_have_title(EXPECTED_TITLE)

    # Remove only Mission 7 state if it exists
    page.evaluate(
        """
        localStorage.removeItem('mission7Hidden');
        """
    )

    page.reload()

    mission7 = page.locator("#search")
    hide_button = page.locator("#persistent-hide-btn")
    result = page.locator("#persistent-hide-result")

    hide_button.click()

    expect(result).to_have_text(
        "Mission 7 is now permanently hidden! "
        "The state is saved in localStorage and will persist after refresh."
    )

    expect(mission7).to_be_hidden()

    page.reload()

    expect(mission7).to_be_hidden()