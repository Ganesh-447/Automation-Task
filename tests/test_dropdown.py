import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_dropdown(browser):
    browser.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
    dropdown = browser.find_element(By.XPATH,"//select[@id ='select-demo']")
    select = Select(dropdown)
    select.select_by_visible_text("Monday")
    time.sleep(3)

    # email_placeholder = email_id.get_attribute('placeholder')
    # assert email_placeholder == 'Email address', 'email address is incorrect'


    #rows = driver.find_elements(By.XPATH, "//table[@class='table table-bordered table-dark']/tbody/tr")
    # row_length = len(rows)
    # print(row_length)
    # cols = driver.find_elements(By.XPATH,"//table[@class='table table-bordered table-dark']/tbody/tr[1]/td[1]")
    # col_length = len(cols)
    # print(f'length of columns {col_length}')
