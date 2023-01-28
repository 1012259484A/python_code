import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By





def test_ceshi_02():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://readhub.cn/topics")
    time.sleep(2)
    #滚动到可视化界面
    el = "window.scrollTo(0,document.body.scrollHeight)"
    #驱动js代码
    driver.execute_script(el)
    time.sleep(3)
if __name__ == '__main__':
    pytest.main("[-s]")
