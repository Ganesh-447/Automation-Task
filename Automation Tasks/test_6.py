from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def find_cell_value(driver,row,col):

    row_index = row + 1
    col_index = col + 1
    cell_path = f"//table[@class='table table-bordered table-dark']/tbody/tr[{row_index}]/td[{col_index}]"
    cell_value = driver.find_element(By.XPATH,cell_path).text
    return cell_value


def test_webtable():
    driver = webdriver.Chrome()
    driver.get('file:///Users/apple/Downloads/AutomationChallenge_2022/QE-index.html')
    driver.maximize_window()
    test_6 = driver.find_element(By.XPATH,"//h1[text()='Test 6']")
    driver.execute_script('arguments[0].scrollIntoView();', test_6)
    assert find_cell_value(driver,2,2) == 'Ventosanzap', 'cell values is not correct'
    time.sleep(2)
    driver.quit()






