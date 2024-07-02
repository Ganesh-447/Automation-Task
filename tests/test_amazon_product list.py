from selenium import webdriver
import pytest


def driver():
    driver = webdriver.Chrome()
    driver.get("")