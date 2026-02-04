# 반복문 - while문

a = 1
print(a)

# a = a + 1
a += 1  #'+=' 복합대입연산자
print(a)

a += 1
print(a)

# 1부터 5까지 출력
# 초기값, 종료값, 증감값
n = 1
while n <= 5:
    print(n)
    n += 1
    
# 5부터 1까지 출력
n = 5
while n >= 1:
    print(n)
    n = n - 1
    
# 1부터 5까지의 합
#  1+2+3+4+5
i = 1
total = 0  #합계를 저장할 변수 선언
while i <= 10:
    # 합계 공식
    # total = total + i
    total += i
    print("i=", i, ", total=", total)
    i += 1
    
print('합계:', total)
