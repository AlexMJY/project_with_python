'''
내부 IP
socket으로 외부사이트에 접속하고 접속된 정보를 바탕으로 IP 확인. 
'''

import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 연결
in_addr.connect(("www.google.co.kr", 443)) # 구글 접속, https 기본 접속 포트 443
print(in_addr.getsockname()[0])