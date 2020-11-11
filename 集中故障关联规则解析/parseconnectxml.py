import json

import pandas as pd
import xmltodict


def pythonXmlToJson():
    with open('5.xml', 'r', encoding='GBK') as f:
        xmlStr = f.read()
    convertedDict = xmltodict.parse(xmlStr)
    jsonStr = json.dumps(convertedDict, indent=1)
    return jsonStr


def main():
    context = pythonXmlToJson()
    data = json.loads(context)
    print(data)
    # print('ruleinfo节点下的数据：', data['xml']['extension']['ruleinfo'])

    # 解析var下的数据
    tag_var = data['xml']['extension']['variables']['var']
    # print('tag_var的类型是：', type(tag_var))

    list = []
    # tag_var:
    for i in tag_var:
        # print(type(i), i)
        list.append(i)

    # 解析ruleinfo下的数据
    tag_ruleinfo = data['xml']['extension']['ruleinfo']
    list.append(tag_ruleinfo)

    # 解析rule下的数据
    tag_rule = data['xml']['rule']['alarm']
    # print('tag_rule的数据是：', tag_rule)
    # print(type(tag_rule))
    tag_rule.pop('keyset')
    list.append(tag_rule)

    # 解析relation下的数据
    tag_relation = data['xml']['rule']['relation']
    print('relation的数据是：', tag_relation)
    print(type(tag_relation))

    list.append(tag_relation[0]['condition'])
    list.append(tag_relation[1]['condition'])

    """tag_relation.pop(1)
    for i in tag_relation:
        list.append(i)"""

    # 解析event下的数据
    tag_event = data['xml']['rule']['relation']
    print('event的数据是：', tag_event)
    print(type(tag_event))

    list.append(tag_event[0]['event']['alarm_new'])
    list.append(tag_event[1]['event']['alarm_rel'])

    df = pd.DataFrame(list)
    # print(list)
    with pd.ExcelWriter('aaa.xls') as Writer:
        df.to_excel(Writer, 'Sheet1', index=False)


if __name__ == '__main__':
    main()
