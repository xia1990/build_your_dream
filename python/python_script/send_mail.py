#!/usr/bin/python
#_*_ coding:utf-8 _*_
#发邮件

import smtplib
from email.mime.text import MIMEText

server="smtp.leyu-tech.com"
port="25"
sender="gaoyuxia@leyu-tech.com"
psw="Wind@4110"
receivers='gaoyuxia@leyu-tech.com,gaoyuxia@wind-mobi.com'
s="TYC-P118F-U000C_V1.0B10_SMT_L0522"
subject="%s生产版本发布" % (s)

url="\\10.0.10.2\人工智能bg软件部\正式软件版本\SDA450\P118F\生产版本\TYC-P118F-U000C_V1.0B10_SMT_L0522"


content1="""
<p>Hi all</p>
<p>生产版本路径:</p>
"""
content2="<p><a href='%s'>%s</a></p>" % (url,url)
content3="<p>麻烦安排可生产测试</p>"

mail_content=content1+"\n"+content2+"\n"+content3

msg=MIMEText(mail_content,"html","utf-8")
msg["from"]=sender
msg["to"]=receivers
msg["subject"]=subject
smtp=smtplib.SMTP()
smtp.connect(server)
smtp.login(sender,psw)
smtp.sendmail(sender,receivers,msg.as_string())
smtp.quit()
