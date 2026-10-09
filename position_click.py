from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        storage_state="auth.json",
    )
    page = context.new_page()

    # Fonction Python appelable depuis la page
    page.expose_function("signaler", lambda x, y: print(f"x={x}, y={y}"))

    # À chaque clic, la page envoie ses coordonnées à Python
    page.add_init_script("""
        document.addEventListener('click', e => {
            window.signaler(e.clientX, e.clientY);
            // Décommente pour empêcher le clic d'agir sur le site :
            // e.preventDefault(); e.stopPropagation();
        }, true);
    """)

    page.goto("https://www.wiki-masters.com/login")
    page.pause()  # garde le navigateur ouvert, ferme la fenêtre pour terminer



    # Eventuellement utiliser 
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
    # à lancer avec "clic_visible(page, 546, 123)" j'ai mis les val de x et y au bol