from playwright.sync_api import sync_playwright
args = (str,)
def main(url:str):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            page.screenshot(path="screenshot.png")
            browser.close()
        return "screenshot.png"
    except:
        return None

