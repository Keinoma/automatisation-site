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


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    #context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.wiki-masters.com/login")

    est_saisie = page.evaluate("""() => {const el = document.activeElement; return el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.isContentEditable; }""")
    
    for i in range(600, 200, -30):
        clic_visible(page, 546, i)
        if est_saisie : 
            break
        else:
            print('cliqué à y: ', i)
        page.wait_for_timeout(800)

    page.keyboard.type("gon", delay=100)
    page.keyboard.type("tra", delay=100) 
    page.keyboard.type("nd", delay=100)  
    page.keyboard.type("TRAND", delay=2000)

    
    page.wait_for_timeout(2000)
    page.mouse.click(19, 32)




    
    #context.tracing.stop(path="trace.zip")
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
