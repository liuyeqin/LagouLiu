#!G:\lagou\venv python
# _*_ coding : utf-8 _*_
from time import sleep
from selenium.webdriver.common.by import By
from Homework.PO.BasePage import Base_Page
from Homework.PO.add_memeber_page import AddMemberPage
from Homework.PO.contact_page import ContactPage


# 主页面封装
class MainPage(Base_Page):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 点击通讯录按钮
    def click_contact(self):
        sleep(10)
        self.find(By.ID, 'menu_contacts').click()
        # 跳转至通讯录页面
        return ContactPage(self.driver)

    # 点击添加成员按钮
    def click_add_member(self):
        sleep(10)
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        # 跳转至添加成员页面
        return AddMemberPage(self.driver)
