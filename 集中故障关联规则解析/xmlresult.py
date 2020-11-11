import json

import pandas as pd
import xmltodict


def pythonXmlToJson():
    with open('abc.xml', 'r', encoding='GBK') as f:
        xmlStr = f.read()
    convertedDict = xmltodict.parse(xmlStr)
    jsonStr = json.dumps(convertedDict, indent=1)
    return jsonStr


context = pythonXmlToJson()
data = json.loads(context)
tag_var = data['xml']['extension']['variables']['var']
print(type(tag_var))
print(tag_var)
list = []
for i in tag_var:
    #print(type(i), i)
    list.append(i)

df = pd.DataFrame(list)
# print(list)
with pd.ExcelWriter('aaa.xls') as Writer:
    df.to_excel(Writer, 'Sheet1', index=False)
