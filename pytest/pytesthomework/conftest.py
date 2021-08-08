#!G:\lagou\venv python
# _*_ coding : utf-8 _*_
import logging
import pytest
from pythoncode.calc import Calculator


# 创建日志收集器
@pytest.fixture(scope='session')
def getlog():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    return logger


# 实例化计算器实例
@pytest.fixture(scope='session')
def getcalc():
    calc = Calculator()
    # 返回计算机实例
    return calc
