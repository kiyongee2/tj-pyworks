# time 모듈
import time

# Unix time -> 1970.1.1 자정이후 시간 초로 환산
print(time.time()) #1769597182.9835355

# tm_year=2026, tm_mon=1, tm_mday=28, tm_hour=19, tm_min=47, tm_sec=16, tm_wday=2, tm_yday=28, tm_isdst=0
print(time.localtime())

# 현재 날짜와 시간을 문자열로 출력
print(time.ctime()) #Wed Jan 28 19:48:16 2026

# 시간 포맷팅
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time) #2026-01-28 19:50:22

# 년과 일로 환산
days = round(time.time() / (24*60*60))
print(days) #20481

years = round(time.time() /(365*24*60*60))
print(years) #56

# sleep(second) - 대기 시간
'''
print("3초 대기 시작...")
time.sleep(3)
print("3초 대기 끝.")
'''

# 수행 시간 측정

start = time.time()  #시작시간
n = 100
for i in range(1, n + 1):
    print(i)
    time.sleep(0.1)

end = time.time() #종료시간
print(f"1부터 {n}까지 출력하는데 걸린 시간: {end-start}초")











