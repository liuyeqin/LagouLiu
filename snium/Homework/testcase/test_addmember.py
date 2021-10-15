#!G:\lagou\venv python
# _*_ coding : utf-8 _*_

'''
【简答题】使用PO设计模式实现企业微信 web 版  添加成员，根据题干要求，在【拉勾系统】的答题框提交gitee或者github代码链接。
'''
import allure
import pytest
from Homework.PO.main_page import MainPage
from Homework.data.getdata import getdata

data = getdata()

# 报告展示
@allure.feature('测试添加成员模块')
class TestAddMember:
    def setup(self):
        # 实例化主页面
        self.main = MainPage()

    def teardown(self):
        self.main = MainPage()

    # 报告里测试用例标题
    @allure.title("测试通讯录页面添加成员成功")
    @pytest.mark.parametrize('member', data['test_success'])
    def test_add_member_succes(self, member):
        m = eval(member)
        result = self.main.click_contact().click_addmember().edit_meber_success(m).get_member_phonenum()
        assert m[2] in result

    @allure.title("测试通讯录页面添加相同ID成员失败")
    @pytest.mark.parametrize('member', data['test_fail'])
    def test_add_member_fail(self, member):
        m = eval(member)
        result = self.main.click_contact().click_addmember().edit_meber_fail(m).get_member_name()
        assert m[0] not in result
