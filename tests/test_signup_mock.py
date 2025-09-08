# tests/test_signup_mock.py

import pytest
from playwright.sync_api import sync_playwright
from web.signup_pw import SignupPage
import json

URL = "file:///C:/Users/uesr/Documents/swtest/web/signup_mock.html"

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

CASES = [
    {
        "id": "success",
        "status": 200,
        "json_body": {"status": "ok", "message": "회원가입 성공(Mocked)"},
        "expected": "회원가입 성공(Mocked)",
    },
    {
        "id": "fail",
        "status": 500,
        "json_body": {"status": "error", "message": "서버 오류(Mocked)"},
        "expected": "서버 오류(Mocked)",
    },
]

@pytest.mark.parametrize("case", CASES)
def test_signup_mock(page, case):

    def fake_signup_api(route, request):
        route.fulfill(
            status=case["status"],
            content_type = "application/json",
            body=json.dumps(case["json_body"]),
        )

    page.route("**/api/signup", fake_signup_api)

    signup = SignupPage(page)
    signup.open(URL)
    signup.fill_form("user@ex.com", "tester","abcd12345","abcd12345", True)
    signup.submit()
    
    flash = signup.flash_message()
    assert case['expected'] in flash