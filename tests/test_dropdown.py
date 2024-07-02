import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_dropdown(browser):
    browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
    dropdown = browser.find_element(By.XPATH,"//select[@id='first']")
    select = Select(dropdown)
    select.select_by_visible_text("Google")
    time.sleep(3)
