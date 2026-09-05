from playwright.sync_api import Playwright, sync_playwright
from loguru import logger

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"],
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.bilibili.com/")
    logger.info(page.title)
    logger.info(page.url)
    logger.info(page.content)
    # input("Press Enter to exit...")
    browser.close()