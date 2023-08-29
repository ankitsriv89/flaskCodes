from playwright.sync_api import sync_playwright

#playwright = sync_playwright().start()

def take_screenshot_from_url(url, session_data):
    with sync_playwright() as playwright:
        for browser_type in [playwright.chromium, playwright.firefox, playwright.webkit]:
            #webkit = playwright.browser_type
            browser = browser_type.launch()
            browser_context = browser.new_context(device_scale_factor=2)
            browser_context.add_cookies([session_data])
            page = browser_context.new_page()
            page.goto(url)
            screenshot_bytes = page.locator(".code").screenshot()
            browser.close()
            return screenshot_bytes
#playwright.stop()