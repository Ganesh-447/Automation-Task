import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_action(browser):
    browser.get("https://awesomeqa.com/practice.html")
    action = ActionChains(browser)
    name = browser.find_element(By.NAME, "firstname")
    action.key_down(Keys.SHIFT).send_keys_to_element(name,"subhash").key_up(Keys.SHIFT).perform()
    time.sleep(4)
