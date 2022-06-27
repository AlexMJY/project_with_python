# 수집한 이메일 주소를 엑셀에 저장
from urllib import response
import requests
import re
from openpyxl import load_workbook
from openpyxl import workbook

url = 'https://news.v.daum.net/v/20220627172955380'

headers = {
    'User-Agent' : 'Mozilla/5.0',
    'Content-Type' : 'text/html; charset=utr-8'
}

reponse = requests.get(url, headers=headers)
results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
print(results)

