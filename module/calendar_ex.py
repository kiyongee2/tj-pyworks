# calendar 모듈 사용
# 2026년 calendar
import calendar

# 2026년 달력
# calendar.prcal(2026)

# 2026년 1월
calendar.prmonth(2026, 2)

# 요일 이름
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print("요일 이름:", calendar.day_name[:])

# 어제의 요일 알아내기
yesterday = calendar.weekday(2026, 1, 26)
print(yesterday) #0(요일의 인덱스)
print(calendar.day_name[yesterday]) #0, Monday

today = calendar.weekday(2026, 1, 27)
print(calendar.day_name[today]) #1, Tuesday

# 설날 첫 휴일의 요일 
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
index = calendar.weekday(2026, 2, 15)
print(index)
print(days[index])