from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_list_group():
    driver = webdriver.Chrome()
    driver.get('file:///Users/apple/Downloads/AutomationChallenge_2022/QE-index.html')
    driver.maximize_window()
    time.sleep(4)
    list_group = driver.find_elements(By.XPATH, "//li[@class='list-group-item justify-content-between']")
    assert len(list_group) == 3, 'list group values are not 3'
    second_list = list_group[1].text
    #print(second_list)
    values = second_list.rsplit(' ',1)
    second_list_item_value = values[0]
    #print(second_list_item_value)
    badge_value = values[1]
    #print(badge_value)
    assert second_list_item_value == 'List Item 2', 'value is not equal to List Item 2'
    assert badge_value == '6', 'badge value is not 6'
    driver.quit()


