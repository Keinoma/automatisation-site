import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    #context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://xn--dmineur-bya.eu/")
    page.get_by_role("button", name="Autoriser").click()
    page.locator("#tile13").click()

    #context.tracing.stop(path="trace.zip")
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
