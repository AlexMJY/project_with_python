import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")

#웹툰 가우스 전자 목록 가져오기

cartoons = soup.find_all("td", attrs={"class":"title"})

title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]

# print(title)
# print("https://comic.naver.com" +link)


# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = cartoon.a["href"]
#     print(title, "https://comic.naver.com" + link)
    
    
    
# rating
cartoons_rate = soup.find_all("div", attrs={"class":"rating_type"})
rating_box = []
for cartoon in cartoons_rate:
    rate = cartoon.find("strong").get_text()
    rating_box.append(float(rate))
    
    
rate_avg = sum(rating_box) / float(len(rating_box))

print(rate_avg)
