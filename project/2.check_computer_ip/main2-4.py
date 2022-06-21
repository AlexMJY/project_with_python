# 외부, 내부 ip 검색
import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 연결
in_addr.connect(("www.google.co.kr", 443)) # 구글 접속, https 기본 접속 포트 443
print(in_addr.getsockname()[0])


req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(out_addr)