import pytest
from playwright.sync_api import sync_playwright
from web.login_pw import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

#파라미터화 
LOGIN_CASES = [("tomsmith","SuperSecretPassword!", "You logged into a secure area!"),
               ("tom","SuperSecretPassword!","Your username is invalid!"),
               ("tomsmith","s","Your password is invalid!"),
               ("","","Your username is invalid!")]

@pytest.mark.parametrize("username,pw,expected",LOGIN_CASES)
def test_login_cases_pw(page,username,pw,expected):
    page = LoginPage(page)
    page.open()
    page.login(username,pw)
    flash = page.flash_message()
    print(f"\nFlash : {flash}")
    assert expected in flash
    