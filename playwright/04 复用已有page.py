from playwright.sync_api import sync_playwright
from loguru import logger

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="../chrome-profile",
        headless=False,
        args=["--start-maximized"],
        no_viewport=True,
        channel="chrome",
    )

    # 复用 Chrome 启动时已有的页面
    page = context.pages[0]

    page.goto("https://www.bilibili.com/")

    logger.info(page.title())
    logger.info(page.url)

    # input("Press Enter to exit...")

    context.close()