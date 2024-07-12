from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_options():
    driver = webdriver.Chrome()
    driver.get('file:///Users/apple/Downloads/AutomationChallenge_2022/QE-index.html')
    driver.maximize_window()
    time.sleep(2)
    Test_3 = driver.find_element(By.XPATH,"//h1[text()='Test 3']")
    driver.execute_script("arguments[0].scrollIntoView();",Test_3)
    time.sleep(2)
    option_1 = driver.find_element(By.XPATH,"//button[@id = 'dropdownMenuButton']")
    assert option_1.text == "Option 1",'Option 1 should be selected by default'
    option_1.click()
    option_3 = driver.find_element(By.XPATH,"//a[text()='Option 3']")
    option_3.click()
    time.sleep(3)
    driver.quit()





