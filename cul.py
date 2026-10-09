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