#!G:\lagou\venv python
# _*_ coding : utf-8 _*_
from time import sleep
from selenium.webdriver.common.by import By
from Homework.PO.BasePage import Base_Page

class AddMemberPage(Base_Page):
    # 添加成员页面，输入必填项
    def edit_meber_success(self, member):
        # 为规避循环导入问题，将导入放入方法内部
        from Homework.PO.contact_page import ContactPage
        sleep(10)
        # 输入姓名
        self.find(By.ID, "username").send_keys(member[0])
        # 输入ID
        self.find(By.ID, "memberAdd_acctid").send_keys(member[1])
        # 输入手机号
        self.find(By.ID, "memberAdd_phone").send_keys(member[2])
        # 点击保存按钮
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # 保存后，跳转回通讯录页面
        return ContactPage(self.driver)

    def edit_meber_fail(self, member):
        sleep(10)
        # 为规避循环导入问题，将导入放入方法内部
        from Homework.PO.contact_page import ContactPage
        # 输入姓名
        self.find(By.ID, "username").send_keys(member[0])
        # 输入ID
        self.find(By.ID, "memberAdd_acctid").send_keys(member[1])
        # 输入手机号
        self.find(By.ID, "memberAdd_phone").send_keys(member[2])
        # 点击保存按钮
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # 点击取消
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        # 保存后，跳转回通讯录页面
        return ContactPage(self.driver)
