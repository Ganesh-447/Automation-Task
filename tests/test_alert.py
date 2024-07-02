from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

def test_aler():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(3)
    button =driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Prompt')]")
    button.click()
    WebDriverWait(driver,10).until(
        EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Ganesh")
    alert.accept()
    time.sleep(3)
