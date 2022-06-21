# 외부 ip
import requests # 사이트에 접속하는 모듈
import re # 정규식

req = requests.get("http://ipconfig.kr") 
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(out_addr)