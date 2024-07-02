from selenium import webdriver
from selenium.webdriver.common.by import By

def test_list_group():
    driver = webdriver.Chrome()
    driver.get('file:///Users/apple/Downloads/AutomationChallenge_2022/QE-index.html')
    list_group = driver.find_elements(By.XPATH, "//li[@class='list-group-item justify-content-between']")
    assert len(list_group) == 3, 'list group values are not 3'
    second_list_item = list_group[1].text
    print(second_list_item)

