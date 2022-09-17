# datetime.date를 통해 year, month, date를 정해줄 수 있음
import datetime

day1 = datetime.date(2019,8,13)
day2 = datetime.date(2021,3,10)

# 두 날짜의 차이는 뺄셈으로 쉽게 구할 수 있음
# day2에서 day1을 빼면 datetime.timedelta 객체가 반환 됨
diff = day2 - day1
# print(diff) 

# datetime.date는 year,month,date로만 구성. hour,minute,second까지 포함하려면 datetime.datetime을 사용
day3 = datetime.datetime(2020, 12, 14, 14, 10, 50)
# print(day3.hour)

# 요일 판별
day_week = day1.weekday()
# print(day_week)

# 오늘 날짜
today = datetime.date.today()

# 오늘로부터 100일 후의 날짜를 얻으려면
diff_days = datetime.timedelta(days=100)
today_after_100 = today + diff_days