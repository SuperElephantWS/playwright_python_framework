import time

from playwright.sync_api import expect


EXPECTED_TITLE = (
    "Playwright, Selenium & Cypress Practice | "
    "Interactive Automation Testing Playground"
)

def test_mission_12(page):

    page.goto(
        "https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html",
        wait_until="domcontentloaded"
    )

    expect(page).to_have_title(EXPECTED_TITLE)
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

    page.locator("#item1").hover()
    # Drag Pizza
    time.sleep(7)  # Wait for the page to load completely
    drag_element(page, "#item1", "#done-column")
    time.sleep(1)
    expect(page.locator("#column-drag-result")).to_have_text(
            "Great! You moved 🍕 Order Pizza to Done!")
    time.sleep(1)

    # Drag Soda
    drag_element(page, "#item2", "#done-column")
    time.sleep(1)
    expect(page.locator("#column-drag-result")).to_have_text(
                "Great! You moved 🥤 Pick up Soda to Done!")
    time.sleep(1)

    # Drag Salad
    drag_element(page, "#item3", "#done-column")
    time.sleep(1)
    expect(page.locator("#column-drag-result")).to_have_text(
                "Great! You moved 🥗 Prepare Salad to Done!")
    time.sleep(1)