from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_verify_elements():
    driver = webdriver.Chrome()
    driver.get('file:///Users/apple/Downloads/AutomationChallenge_2022/QE-index.html')
    driver.maximize_window()
    email_id = driver.find_element(By.XPATH,"//input[@type='email']")
    password = driver.find_element(By.XPATH,"//input[@type='password']")
    login = driver.find_element(By.XPATH,"//button[@type='submit']")
    assert email_id is not None, "email_id input is not present"
    assert password is not None, "password input is not present"
    assert login is not None, "login button is not present"
    email_id.send_keys('test123@gmail.com')
    password.send_keys('test123')
    time.sleep(3)
    driver.quit()

