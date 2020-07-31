"""
zabbix发送告警到钉钉的脚本，自己云主机用
"""
import requests
import json
import sys
import os
import datetime
webhook = "https://oapi.dingtalk.com/robot/send?access_token=e3a59845e29c57c53760fea653f9de28c6da4d68b1af6fa2d511baf8796db262"
user = sys.argv[1]
text = sys.argv[2]
data = {
    "msgtype": "text",
    "text": {
        "content": text
    },
    "at": {
        "atMobiles": [
            user
        ],
        "isAtAll": False
    }
}
headers = {'Content-Type': 'application/json'}
x = requests.post(url=webhook, data=json.dumps(data), headers=headers)
if os.path.exists(r"C:/dingding.log"):
    f = open(r"C:/dingding.log", "a+")
else:
    f = open(r"C:/dingding.log", "w+")
f.write("\n"+"--"*30)
print(x.json())
if x.json()["errcode"] == 0:
    f.write("\n"+str(datetime.datetime.now())+"    " +
            str(user)+"    "+"发送成功"+"\n"+str(text))
    f.close()
else:
    f.write("\n"+str(datetime.datetime.now()) + "    " +
            str(user) + "    " + "发送失败" + "\n" + str(text))
    f.close()
