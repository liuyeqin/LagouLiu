import yaml


def getdata():
    add_ids = []
    div_ids = []
    # 读取数据文件
    with open(r"../datas/calc.yml", encoding='utf-8') as f:
        f_data = yaml.safe_load(f)
        # 获取加法数据字典
        add = f_data['add']
        # 获取除法数据字典
        div = f_data['div']
        # 获取加法数据列表
        add_datas = add['datas']
        # 生成加法ids
        for i in add_datas:
            ids_v = str(i[0]) + '+' + str(i[1])
            add_ids.append(ids_v)
        # 获取除法列表
        div_datas = div['datas']
        # 生成除法ids
        for i in div_datas:
            ids_v = str(i[0]) + '/' + str(i[1])
            div_ids.append(ids_v)
    # 返回加法数据，加法ids,除法数据，除法ids
    return add_datas, add_ids, div_datas, div_ids
