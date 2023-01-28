import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




def test_ceshi_03():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("file:///D:/python_code/2023-1-27/test_js.html")
    f = driver.find_element(By.ID,'kw')
    f.send_keys(r'D:\python_code\2023-1-27\总结')
    time.sleep(3)
if __name__ == '__main__':
    pytest.main("[-s]")
