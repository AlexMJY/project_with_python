# 정규식을 이용하여 이메일의 형식을 추출하는 코드
import re


test_string = """
aaa@@@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kor
"""

results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)
print(results)