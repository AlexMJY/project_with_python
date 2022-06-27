#리스트에서 중복된 내용을 제거 : use set()
import re
from unittest import result

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
results = list(set(results))
print(results)