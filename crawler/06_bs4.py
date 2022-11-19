import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 가져온 문서를 lxml paser를 통해 BS 객체를 만들었다.
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element를 반환
# print(soup.a.attrs) # a element의 attrs(속성)들을 반환
# print(soup.a['onclick']) # 원하는 attrs values 뽑아내기


# print(soup.find(attrs={"class" : "Nbtn_upload"})) # class : Nbtn_upload가 하나밖에 없기 때문에 tag a를 생략해도 된다.
# print(soup.find("a", attrs={"class" : "Nbtn_upload"}))


# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.get_text())

# rank2 = rank1.find_next_sibling("li")
# rank3 = rank2.find_next_sibling("li")
# rank4 = rank3.find_next_sibling("li")
# rank5 = rank4.find_next_sibling("li")
# rank3 = rank5.find_previous_sibling("li")

# rank_all = rank1.find_next_siblings("li")

# webtoon = soup.find("a", text="소녀재판-125화")
# print(webtoon)