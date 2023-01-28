import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def  test_ceshi():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.12306.cn/index/")
    #操作时间控件
    driver.find_element(By.ID,'train_date').click()
    driver.find_element(By.XPATH,"//*[@id='toolbar_Div']/div[10]/div[1]/div[2]/div[31]/div").click()
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    pytest.main("[-s]")
