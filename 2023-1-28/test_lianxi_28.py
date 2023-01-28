import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By




class Test_lonin:

    def test_ceshi_03(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.ketangpai.com/#/login")
        driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div/div/form/div[1]/div/div/input').send_keys("13143364918")
        driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/input').send_keys("lidaye000")
        danji = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/button')
        #使用JS代码操作
        driver.execute_script('arguments[0].click()',danji)
        time.sleep(3)


    def test_ceshi_04(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.ketangpai.com/#/login")
        danji = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/button')
        #使用JS代码操作
        driver.execute_script('arguments[0].click()',danji)
        time.sleep(2)
        #实际结果
        error_one = driver.find_elements(By.CLASS_NAME,'el-form-item__error')
        #预期结果
        error_tow = ['请输入密码']
        #判断预期结果与实际结果是否一致
        for index,el in enumerate(error_one):
            assert el.text == error_tow[index]

    if __name__ == '__main__':
        pytest.main("[-s]")
