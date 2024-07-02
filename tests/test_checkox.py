import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    cbox = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
    for i in cbox:
        if not i.is_selected():
            i.click()
        elif i.is_selected():
            i.click()
    time.sleep(3)