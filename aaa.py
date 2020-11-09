import os
import json

with open('./data1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    result = {}  # 定义一个空字典
    string = []
    for l in lines:
        l = l.strip("\n")
        string.append(l)
    # print(string)
    jas = json.dumps(string)
    print(jas)
    # print(f.read())
