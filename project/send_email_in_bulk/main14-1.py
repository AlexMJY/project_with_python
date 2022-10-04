# 네이버 메일을 보내는 코드 

import smtplib
from email.mime.text import MIMEText

send_email = "naver_id@naver.com"
send_pw = "naver_pw"

recv_email = "recv_id@naver.com"

smtp_name = "smtp.naver.com" # naver_mail smtp
smtp_port = 587 # naver_mail port

text = """
~~
"""

msg = MIMEText(text)

msg['Subject'] = 'Mail Subject'
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pw)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()