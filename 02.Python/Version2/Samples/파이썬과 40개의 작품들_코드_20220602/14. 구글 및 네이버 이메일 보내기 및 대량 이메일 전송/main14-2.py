import smtplib
from email.mime.text import MIMEText

send_email = "munjjac@gmail.com"
send_pwd = "xcxxkcurqfzertmt"

recv_email = "munjjac@hanmail.net"

smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
메일 내용을 여기에 적습니다.
여러줄을 입력하여도 됩니다.
"""
msg = MIMEText(text)

msg['Subject'] ="메일제목은 여기에 넣습니다"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()