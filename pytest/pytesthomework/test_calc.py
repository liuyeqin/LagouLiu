#!G:\lagou\venv python
# _*_ coding : utf-8 _*_

'''
1、补全计算器（加法，除法）的测试用例

2、使用数据驱动完成测试用例的自动生成

3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
'''

import allure
import pytest
from pytesthomework.commons import getdata


# 报告展示
@allure.feature('测试计算器')
# 定义测试用例类
class TestCalc:
    # 获取参数
    add_datas, add_ids, div_datas, div_ids = getdata()

    # 报告里测试用例标题
    @allure.title("测试相加_{a}_{b}_{expect}")
    # 测试用例参数化
    @pytest.mark.parametrize('a,b,expect', add_datas, ids=add_ids)
    # 加法测试用例
    def test_add(self, a, b, expect, getcalc, getlog):
        """

        :param a: 参数a int float
        :param b: 参数b int float
        :param expect: 期望结果，int float
        :param getcalc: 计算器类实例
        :param getlog: 日志实例
        :return: none
        """
        # 调用被测函数，得到实际结果
        result = getcalc.add(a, b)
        getlog.info(f"实际结果{a}+{b}={result}")
        # python机制问题，对float做转换
        if isinstance(result, float):
            result = round(result, 10)
            getlog.info(f"浮点数保留精度后{result}")
        # 断言实际结果与期望结果
        assert result == expect

    # 报告里测试用例标题
    @allure.title("测试除法_{a}_{b}_{expect}")
    # 参数化
    @pytest.mark.parametrize('a,b,expect', div_datas, ids=div_ids)
    # 除法测试用例
    def test_div(self, a, b, expect, getcalc, getlog):
        """

        :param a: 参数a int float
        :param b: 参数b int float
        :param expect: 期望结果，int float
        :param getcalc: 计算器类实例
        :param getlog: 日志实例
        :return: none
        """
        # 判断被除数是否为0
        if b != 0:
            # 调用被测函数，得到实际结果
            result = getcalc.div(a, b)
            getlog.info(f"实际结果{a}/{b}={result}")
            # 断言实际结果与期望结果
            assert result == expect
        else:
            try:
                result = getcalc.div(a, b)
            except Exception as e:
                getlog.error(e)
