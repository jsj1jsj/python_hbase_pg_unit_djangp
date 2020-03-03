# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 14:21
# @Author  : billy
# @File    : send_email.py


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from common import globalB
from email import encoders

def _format_addr(s):
    name, addr = parseaddr ( s)
    return formataddr ((Header (name, 'utf-8 ').encode(), addr ))

def sendmail(pic_path):
    # 发件人地址
    from_addr = 'service.xunfei@nyintel.com'
    # 邮箱密码
    password = 'Xunfei1234'
    # 收件人地址,可同时添加多个
    to_addrs = [
        'wang.huijun@nyintel.com','wanghuijun@chinacfsc.com'
    ]
    # 邮箱服务器地址
    smtp_server = 'smtp.exmail.qq.com'
    server_addr = "https://www.cnblogs.com/wyongbo/p/python_send_email.html"
    # server_addr = ReadConfig().get_config( "server_addr", "ip" )

    # 创建一个邮件内容的实例
    mail_msg = MIMEMultipart()
    # 设置邮件的标题
    mail_header = 'UI自动化'
    mail_msg['Subject'] = Header(mail_header, 'utf-8')

    # 设置邮件的正文(html格式)
    mail_body ="""<html>
                  <body>
                    <H3>UI测试</H3>
                    <a href="http://127.0.0.1:8000/show" target="_blank"><button type="button">点击查看详细报告</button></a>
                    <p><img src="cid:imageid" alt="imageid"></p>
                  </body>
                  </html>
              """
    html_report = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    mail_msg.attach(html_report)  # 读取的报告写在邮件内容中

    file = open(pic_path, "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    mail_msg.attach(img)


    # mail_msg['From'] = from_addr
    # mail_msg['To'] = ','.join(to_addrs)

    #创建一个连接
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(from_addr, password)
        # smtp.sendmail(from_addr, mail_msg['To'].split(','), mail_msg.as_string())
        smtp.sendmail(from_addr, to_addrs=to_addrs, msg=mail_msg.as_string())
        print("邮件发送")
        smtp.quit()
    except smtplib.SMTPException as e:
        print("邮件发送失败，失败原因：%s" % e)

if __name__ == '__main__':
    sendmail(r"D:\xunfei20200117bk\XunFei\report_png\result.png")

