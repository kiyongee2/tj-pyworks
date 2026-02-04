# 날짜와 시간 모듈 - datetime 
# 패키지 - 여러 모듈을 묶은 디렉터리 구조이다.
"""
 import 모듈이름
 from 패키지이름 import 모듈이름
"""

import datetime 
# 현재 날짜와 시간
now = datetime.datetime.today() #2026-01-27 21:20:13.712903
print(now)

from datetime import datetime, date

now = datetime.today() #2026-01-27 21:20:13.712903
print(now)

# 년, 월, 일 출력
print(now.year, now.month, now.day)

# 시, 분 , 초
print(now.hour, now.minute, now.second)

# 특정한 날짜 설정
the_day = date(2026, 2, 15)
print(the_day) #2026-02-15

today = date.today()
print(today) #2026-01-27

# DDay 계산
remain_day = the_day - today 
print(f"설날까지 {remain_day.days}일 남았습니다.")
