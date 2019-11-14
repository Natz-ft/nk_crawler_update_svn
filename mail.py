# coding:utf-8
# coding in python 3.7

import os
import traceback
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart

##########
"""
版本v1.0说明
1. 支持多人抄送
2. 支持单个附件
"""
##########
class Mail(object):
    def __init__(self, smtp_server: str, username: str, password: str, from_addr: str, to_addr: str, cc_addr: str, subject: str, \
                   content: str, attach_file: str, content_type="utf-8", port=587, need_auth=True):
        """
        :param smtp_server: 服务器的地址,如 ：“mail.northking.net"
        :param username: 如northking邮箱的用户名
        :param password: password
        :param from_addr: 发送方邮件地址
        :param to_addr: 接收方邮件地址,字符串，用";"分隔,"one@qq.com;two@northking.net",不要有空格
        :param cc_addr: 抄送者,如"one@qq.com;two@northking.net"
        :param subject: 邮件主题
        :param content: 邮件内容
        :param content_type: 编码方式,默认"utf-8"
        :param attach_file: 邮件附件路径 ,"绝对路径"
        :param port: 默认587
        :param need_auth: 授权...,暂时没用到
        """
        self.smtp_ser = smtp_server
        self.use_name = username
        self.passwd = password
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.cc_addr = cc_addr
        self.subject = subject
        self.content = content
        self.content_type = content_type
        self.attach_file = attach_file  # 要解决没有附件问题
        self.port = port
        self.need_auth = need_auth

    def send_email(self):
        # 邮件发送和接收人配置
        msg = MIMEMultipart()
        msg['From'] = self.from_addr # 显示的发件人
        msg['To'] = self.to_addr
        if len(self.cc_addr.strip()) > 0:
            msg['Cc'] = self.cc_addr
        msg['Subject'] = Header(self.subject, 'utf-8')  # 显示的邮件标题

        # 需要传入的路径
        if not self.attach_file:  # 无附件时候
            msg.attach(MIMEText('no attach file...', self.content_type, 'utf-8'))

        else:  # 有附件
            r = os.path.exists(self.attach_file)
            if r is False:
                msg.attach(MIMEText('no attach file...', self.content_type, 'utf-8'))
                print("文件读取 error")
            else:
                # 邮件正文是MIMEText:
                msg.attach(MIMEText(self.content.strip(), self.content_type, 'utf-8'))
                filepart = MIMEApplication(open(self.attach_file, 'rb').read())
                filepart.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.attach_file))
                msg.attach(filepart)

        try:
            server = smtplib.SMTP(host=self.smtp_ser, port=self.port)
            # server.set_debuglevel(1)  # 用于显示邮件发送的执行步骤
            # server.ehlo()
            # 如果是一般的smtp发送邮件，可以把下面一句注释
            server.starttls()
            # server.ehlo()
            server.login(self.use_name, self.passwd)
            _receive_addr = self.make_addr_list()  # 接受人地址list
            server.sendmail(self.from_addr, _receive_addr, msg.as_string())
            server.quit()
            print("发送完毕")

        except Exception as e:
            print("Error: unable to send email")
            traceback.print_exc()

    def make_addr_list(self):
        """将地址加工成发送地址，list格式"""
        _to_addr = self.to_addr.split(";")
        _cc_addr = self.cc_addr.split(";")
        return _to_addr + _cc_addr


if __name__ == "__main__":
    smtp_host_server = "mail.northking.net"
    usr_name = "zbpc"
    passwd = "zbpc123456"
    from_addr = "zbpc@northking.net"
    to_addr = "fei.yang@northking.net"
    # cc_addr = "jinlong.wu@northking.net"
    cc_addr = "jinlong.wu@northking.net"
    subject = "爬虫测试"
    content = "爬虫测试"
    content_type = "utf-8"
    # attachfile = r"C:\Users\yahuu\Pictures\11.jpg"
    attachfile = r"C:\Users\Teddy\Desktop\SeparWords_merge_result.xls"
    # attachfile = ""
    port = 587

    mail = Mail(smtp_server=smtp_host_server,
                    username=usr_name,
                    password=passwd,
                    from_addr=from_addr,
                    to_addr=to_addr,
                    cc_addr=cc_addr,
                    subject=subject,
                    content=content,
                    content_type=content_type,
                    attach_file=attachfile,
                    port=587)
    mail.send_email()
