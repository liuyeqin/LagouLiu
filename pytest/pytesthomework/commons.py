import yaml


def getdata():
    add_ids = []
    div_ids = []
    with open(r"../datas/calc.yml", encoding='utf-8') as f:
        f_data = yaml.safe_load(f)
        add = f_data['add']
        div = f_data['div']
        add_datas = add['datas']
        for i in add_datas:
            ids_v = str(i[0]) + '+' + str(i[1])
            add_ids.append(ids_v)

        div_datas = div['datas']
        for i in div_datas:
            ids_v = str(i[0]) + '/' + str(i[1])
            div_ids.append(ids_v)

    return add_datas, add_ids, div_datas, div_ids
