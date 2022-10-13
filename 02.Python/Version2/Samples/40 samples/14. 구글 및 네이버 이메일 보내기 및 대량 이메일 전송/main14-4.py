import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email = "보내는메일주소"
send_pwd = "비밀번호"

recv_email = "받는메일주소"

smtp_name = "smtp.naver.com" 
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] ="html로 보내는 메일 입니다."
msg['From'] = send_email 
msg['To'] = recv_email 

html_body = """
<p>안녕하세요 html 형식으로 보내는 이메일 테스트 입니다.</p>
<p><span style="color: #0000ff;">글자의 색상을 지정하거나</span></p>
<h1>크기를 조정할수 있습니다.</h1>
<p>표도 만들수 있습니다.</p>
<table style="height: 83px;" width="241">
<tbody>
<tr>
<td style="width: 73px;">1</td>
<td style="width: 73px;">2</td>
<td style="width: 73px;">3</td>
</tr>
<tr>
<td style="width: 73px;">표를</td>
<td style="width: 73px;">만들수&nbsp;</td>
<td style="width: 73px;">있습니다.</td>
</tr>
<tr>
<td style="width: 73px;">4</td>
<td style="width: 73px;">5</td>
<td style="width: 73px;">6</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
"""

msg.attach( MIMEText(html_body,'html') ) 

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()