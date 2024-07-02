import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_apexon(driver):
    load_dotenv()
    driver.get(os.getenv('URL'))
    email = driver.find_element(By.XPATH,"//input[@id='login-username']")
    email.send_keys(os.getenv('EMAIL'))
    password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
    password.send_keys(os.getenv('PASSWORD'))
    button = driver.find_element(By.XPATH,"//button[@id ='js-login-btn']")
    button.click()
    WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element((By.XPATH,"//h1[contains(text(),'Dashboard')]"),'Dashboard')
    )
    elemt = driver.find_element(By.XPATH,"//span[contains(@data-qa,'lufexuloga')]")
    a =elemt.text
    assert a == 'Aman', 'username is wrong'

