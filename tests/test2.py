from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

def test():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv('URL'))
    email = driver.find_element(By.CSS_SELECTOR, "input[id ='login-username']")
    password = driver.find_element(By.XPATH, "//input[@id ='login-password']")
    email.send_keys(os.getenv('EMAIL'))
    login = driver.find_element(By.XPATH, "//button[@id ='js-login-btn']")
    password.send_keys(os.getenv('PASSWORD'))
    login.click()
    WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element((By.XPATH,"//h1[@class='page-heading']"),'Dashboard'))

    verificat = driver.find_element(By.XPATH, "//span[@class='Fw(semi-bold) ng-binding']")
    assert verificat.text == 'Aman', 'not matched'
    print(driver.title)
    time.sleep(3)

