# 내장 함수(Built in Function)
a = [1, 2, 3, 4]

# 합계
print(sum(a)) #10

# 최대값, 최소값
print(max(a), min(a)) #4, 1

# 반올림 - 정수로 표시
print(round(2.746)) #3
print(round(2.146)) #2

x = 706.351
print(round(x, 1)) #소수첫째자리 706.4
print(round(x, 0)) #706.0 (실수)
print(round(x)) #706(정수)
print(round(x, -1)) #710.0
print(round(x, -2)) #700.0

# 절대값 - abs() : 양수를 입력하면 양수, 음수를 입력해도 양수 반환
print(abs(8))  #8
print(abs(-8)) #8

# 절대값 함수 정의
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

print(my_abs(-8))
print(my_abs(8))
