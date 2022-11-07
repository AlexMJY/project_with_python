import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 가져온 문서를 lxml paser를 통해 BS 객체를 만들었다.
print(soup.title)