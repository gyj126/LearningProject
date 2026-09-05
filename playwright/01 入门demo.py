from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False, # 默认无头，这里显式使用有头，便于排查
        channel="chrome", # 模式使用自带的浏览器，这里使用系统安装的浏览器
    )

    page = browser.new_page()

    page.goto("https://www.bilibili.com/")

    print(page.title())
    print(page.url)
    # print(page.content())
    input("Press Enter to exit...")
    browser.close()