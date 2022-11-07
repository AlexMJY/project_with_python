Web Crawler
=============

## Chrome Driver 다운로드 

버전 확인 후 [크롬드라이버 다운로드 페이지](https://chromedriver.chromium.org/downloads)에서 버전에 맞게 설치한다.

<버전이 틀릴 경우 발생하는 error message>
    selenium.common.exceptions.SessionNotCreatedException:Message: session not created: This version of ChromeDriver only supports Chrome version 90 Current browser version is 94.0.4606.71 with binary path /Applications/Google Chrome.app/Contents/MacOS/Google Chrome


- 정적 웹 크롤링
    - 원하는 웹 페이지의 html 문서를 긁어온다.
    - 긁어온 html 문서를 parsing한다.
    - parsing한 html문서에서 원하는 것을 골라서 사용한다.

## requests 사용 방법
    import requests               

    가져올 url 문자열로 입력
    url = 'https://www.naver.com'  

    requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)    

    우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text


## BeautifiulSoup4 사용 방법
    from bs4 import BeautifulSoup as bs
    
    html = bs(html_text, 'html.parser)

    사용 함수 목록
    [find(), find_all(), select(), select_one()]