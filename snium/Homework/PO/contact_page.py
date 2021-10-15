#!G:\lagou\venv python
# _*_ coding : utf-8 _*_
from time import sleep

from selenium.webdriver.common.by import By
from Homework.PO.BasePage import Base_Page
from Homework.PO.add_memeber_page import AddMemberPage


class ContactPage(Base_Page):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    # 通讯录页面，点击添加成员
    def click_addmember(self):
        sleep(10)
        self.find(By.CSS_SELECTOR,".js_add_member:nth-child(2)").click()
        #self.driver.find_element(By.XPATH,"#").click()
        # 跳转至添加成员页面
        return AddMemberPage(self.driver)

    def get_member_phonenum(self):
        sleep(10)
        # 获取成员手机号
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        # 列表推导式，将title属性提取出来
        num_list = [i.get_attribute("title") for i in eles]
        #print(name_list)
        return num_list

    def get_member_name(self):
        sleep(10)
        # 获取成员名字
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 列表推导式，将title属性提取出来
        name_list = [i.get_attribute("title") for i in eles]
        #print(name_list)
        return name_list