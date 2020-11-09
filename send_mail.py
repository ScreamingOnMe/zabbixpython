#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
zabbix发送告警到邮件的脚本，自己云主机用
"""
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import sys

smtpaddr = 'smtp.boco.com.cn'
myemail = 'lijian@boco.com.cn'
password = r'JLwg!2018'
recvmail = sys.argv[1]
subject = sys.argv[2]
content = sys.argv[3]

msg = MIMEText("""%s""" % (content), "plain", "utf-8")
msg['Subject'] = Header(subject, 'utf-8').encode()
msg['From'] = myemail
msg['To'] = recvmail

try:
    smtp = SMTP_SSL(smtpaddr)
    smtp.login(myemail, password)
    smtp.sendmail(myemail, recvmail.split(','), msg.as_string())
    smtp.quit()
    print("success")
except Exception as e:
    print("fail: "+str(e))
