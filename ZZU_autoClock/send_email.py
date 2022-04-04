from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.utils import formataddr

def send_mail(tiltle, body):
    # 设置 QQ邮箱
    my_sender = 'xxx@qq.com' # 发件人邮箱账号
    my_pass = 'ahfhf'   # 发件人邮箱授权码，可以查看QQ邮箱官方的说明，其他邮箱亦可自行配置
    my_user = 'xxxx@qq.com'  # 接收信息的邮箱，最好为本人 QQ邮箱，首次接收邮件需要从垃圾信件中移出

    # 设置发送消息
    msg = MIMEText(body, 'plain', 'utf-8') # 正文
    msg['From'] = formataddr(['ZZU 自动健康打卡器', my_sender]) # 设置发件人
    msg['To'] = formataddr(['尊贵的用户', my_user]) # 设置收件人
    msg['Subject'] = tiltle # 设置标题

    # 发送邮件
    server = SMTP_SSL('smtp.qq.com', 465) # 设置 QQ邮箱 SMTP 服务器地址和端口
    server.login(my_sender, my_pass) # 链接 SMTP 服务
    server.sendmail(my_sender, [my_user, ], msg.as_string()) # 发送邮件

    # 关闭连接
    server.quit()


# for test
if __name__ == '__main__':
    send_mail('title', 'body')
