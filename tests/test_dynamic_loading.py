# tests/test_dynamic_loading.py

import pytest
from playwright.sync_api import sync_playwright

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
EXPECTED = "Hello World!"

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

def test_dynamic_loading_pw(page):
    page.goto(URL)
    page.click("#start button")

    msg = page.locator("#finish").inner_text().strip()

    assert EXPECTED in msg



#########################################
# selenium 
##########################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_dynamic_loading_se(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    finish = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    # finish = driver.find_element(By.ID, "finish")
    assert EXPECTED in finish.text.strip()
