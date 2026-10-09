import os
import re
from playwright.sync_api import Playwright, sync_playwright, expect

def clic_visible(page, x, y, duree_ms=1500):
    page.evaluate("""([x, y, duree]) => {
        const point = document.createElement('div');
        point.style.cssText = `
            position: fixed;
            left: ${x - 8}px;
            top: ${y - 8}px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: rgba(255, 0, 0, 0.7);
            border: 2px solid white;
            z-index: 2147483647;
            pointer-events: none;
        `;
        document.body.appendChild(point);
        setTimeout(() => point.remove(), duree);
    }""", [x, y, duree_ms])
    page.mouse.click(x, y)

def est_saisie(page):
    return page.evaluate("""() => {const el = document.activeElement; return el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.isContentEditable; }""")
    

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    #context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.wiki-masters.com/login")
    page.wait_for_timeout(1000)

   
    while not est_saisie(page):
        clic_visible(page, 546, 240)
        page.wait_for_timeout(800)
    page.keyboard.type("gontranductible@gmail.com", delay=100)
    page.wait_for_timeout(500)    


    clic_visible(page, 540, 350)
    while not est_saisie(page):
        clic_visible(page, 540, 350)
        page.wait_for_timeout(800)
    page.keyboard.type(os.environ["WIKI_PASSWORD"], delay=100)

    
    
    
    #context.tracing.stop(path="trace.zip")
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
