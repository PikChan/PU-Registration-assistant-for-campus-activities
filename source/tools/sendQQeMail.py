from email.header import Header

from email.mime.text import MIMEText

from email.utils import parseaddr, formataddr

import smtplib
from smtplib import SMTP_SSL

class QQMail :
    sendAddr = ""
    targetAddr= ""
    qqmail_stmp_code= ""
    serverDomain= ""
    sendName= ""
    # mailContent= ""

    def __init__(self):
        self.sendAddr = "gcxg@qq.com"
        self.sendName = "编号1667"
        self.targetAddr = "zbc7@qq.com"
        self.qqmail_stmp_code = "chwwtqhiodphbdid"  # "zoevfqwtswqibfic"
        self.serverDomain = "smtp.qq.com"

    def send_mail(self,content):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.sendAddr
        msg['To'] = self.targetAddr
        msg['Subject'] = Header('有新活动发布', 'utf-8').encode()
        server: SMTP_SSL = smtplib.SMTP_SSL(self.serverDomain, 465)
        server.login(self.sendAddr, self.qqmail_stmp_code)
        server.sendmail(self.sendAddr, self.targetAddr, msg.as_string())
        server.quit()
        print('邮件发送成功！')



