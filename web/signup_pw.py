# web/signup_pw.py

from playwright.sync_api import sync_playwright, Page

URL = "file:///C:/Users/uesr/Documents/swtest/web/signup.html"

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        # 요소 locator
        self.email = page.locator("#email")
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.confirm = page.locator("#confirm")
        self.terms = page.locator("#terms")
        self.submit_btn = page.locator("button[type=submit]")
        self.flash = page.locator("#flash")

    def open(self, url=URL):
        self.page.goto(url)

    def fill_form(self, email, username, password, confirm, terms=True):
        self.email.fill(email)
        self.username.fill(username)
        self.password.fill(password)
        self.confirm.fill(confirm)
        if terms:
            self.terms.check()
        else:
            self.terms.uncheck()

    def submit(self):
        self.submit_btn.click()

    def flash_message(self) -> str:
        self.flash.wait_for(state='visible')
        return self.flash.inner_text().strip()
        # msg = self.page.locator(self.flash).inner_text()
        # return msg.strip()


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        signup = SignupPage(page)
        signup.open()
        signup.fill_form(
            email="user@example.com",
            username="tester",
            password="abc12345",
            confirm="abc12345",
            terms=True,
        )
        signup.submit()
        print("Flash message:", signup.flash_message())

        browser.close()