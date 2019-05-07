#!/usr/bin/python
#_*_ coding:utf-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.wind-mobi.com"
mail_user="gaoyuxia@wind-mobi.com"
mail_pass="gyx@4110"

sender="gaoyuxia@wind-mobi.com"
receivers=["gaoyuxia@wind-mobi.com"]
message=MIMEText("Python邮件发送测试...",'plain','utf-8')
message['From']=Header("菜鸟教程 ","utf-8")
message["To"]=Header("测试","utf-8")
subject="Python SMTP 邮件测试"
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP("")
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error:无法发送邮件"
