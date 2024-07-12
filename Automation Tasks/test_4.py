from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_button():
    driver = webdriver.Chrome()
    driver.get('file:///Users/apple/Downloads/AutomationChallenge_2022/QE-index.html')
    driver.maximize_window()
    test_4 = driver.find_element(By.XPATH, "//h1[text()='Test 4']")
    driver.execute_script('arguments[0].scrollIntoView();', test_4)
    button_1 = driver.find_element(By.XPATH, "//h1[text()='Test 4']/following-sibling::button[@class='btn btn-lg btn-primary']")
    assert button_1.is_enabled(), 'First button is not enabled'
    button_2 = driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-secondary']")
    assert not button_2.is_enabled(), 'Second button is enabled'
    time.sleep(2)
    driver.quit()

