#!G:\lagou\venv python
# _*_ coding : utf-8 _*_
import yaml


def getdata():
    with open(r"../data/data.yaml",encoding='utf-8') as f:
        f_data = yaml.safe_load(f)
        #f_data['test_success'][0]
        #print(f_data['test_success'],f_data['test_fail'])
        return f_data
            #f_data['test_success'],f_data['test_fail'],f_data['main_test_success']