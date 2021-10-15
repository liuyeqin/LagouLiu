#!G:\lagou\venv python
# _*_ coding : utf-8 _*_

# 封装和页面，即测试内容无关的公共方法
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base_Page:
    _base_url = ""

    # 复用浏览器方法
    def __init__(self, base_driver=None):
        if base_driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(10)

        else:
            self.driver: webdriver = base_driver

    def find(self,by,locator = None):
        # 定义driver.self.find_element 为公共方法
        if locator == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by = by,value = locator)
