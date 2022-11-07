from cgitb import html
import requests

url = "https://www.naver.com"

response = requests.get(url)

html_text = response.text

# print(html_text)

from bs4 import BeautifulSoup as bs

html = bs(html_text, 'html.parser')