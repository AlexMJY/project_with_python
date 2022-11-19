import requests
res = requests.get("http://google.com")
# print("status code: ", res.status_code)

# if res1.status_code == requests.codes.OK:
#     print("정상입니다.")
# else:
#     print("비정상입니다.")

res.raise_for_status() # status code가 400대일 경우 error를 내고 프로그램 

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)