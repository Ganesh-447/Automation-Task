from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_button():
    driver = webdriver.Chrome()
    driver.get('file:///Users/apple/Downloads/AutomationChallenge_2022/QE-index.html')
    driver.maximize_window()
    test_5 = driver.find_element(By.XPATH,"//h1[text()='Test 5']")
    driver.execute_script('arguments[0].scrollIntoView();',test_5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//h1[text()='Test 5']/following-sibling::button[@class='btn btn-lg btn-primary']")))
    button = driver.find_element(By.XPATH, "//h1[text()='Test 5']/following-sibling::button[@class='btn btn-lg btn-primary']")
    button.click()
    message = driver.find_element(By.XPATH, "//div[@class='alert alert-success']")
    assert message.text == 'You clicked a button!', 'click was not happened correctly'
    assert not button.is_enabled(),'button is not disabled'
    time.sleep(3)
    driver.quit()


