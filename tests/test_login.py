#tests/test_login.py

import pytest
from web.login import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="session")
def driver():
    opts = Options()
    # $env:HEADLESS="true"
    if os.getenv("HEADLESS","false").lower() == "true":
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(opts)
    yield driver
    driver.quit()

# #autouse=True:모든 테스트 함수(파라미터 각 케이스 포함) 앞에서 자동 실행됩니다.
@pytest.fixture(autouse=True)  
def reset_state(driver):
    driver.delete_all_cookies() # 쿠키/스토리지 정리
    driver.get("about:blank")
    yield

LOGIN_CASES = [("tomsmith","SuperSecretPassword!", "You logged into a secure area!"),
               ("tom","SuperSecretPassword!","Your username is invalid!"),
               ("tomsmith","s","Your password is invalid!"),
               ("","","Your username is invalid!")]
@pytest.mark.parametrize("username,pw,expected", LOGIN_CASES)
def test_login_cases(driver, username,pw,expected):
    page = LoginPage(driver)
    page.open()
    page.login(username,pw)
    msg = page.flash_message()
    print(f"flash msg : {msg}")
    assert expected in msg
