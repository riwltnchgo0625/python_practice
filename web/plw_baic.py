# web/plw_basic.py

# pip install playwright
# playwright install 

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        print( page.title() )
        page.screenshot(path="screenshot.png")

def mrun():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page1 = browser.new_page()
        page1.goto("https://google.com")
        print( page1.title() )

        page2 = browser.new_page()
        page2.goto("https://www.naver.com")
        print( page2.title() )

        # input()

if __name__ == "__main__":
    mrun()