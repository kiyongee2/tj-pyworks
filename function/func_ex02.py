# return이 있는 함수
# 응원 메시지를 보내는 함수
def message():
    return "행운을 빌어요!"

# 제곱 계산 함수
def square(x):
    return x * x

# 두 수를 더하는 함수
def add(x, y):
    return x + y

# 메인 영역
msg = message() #문자열 반환받음
print(msg)

value1 = square(4) #16을 반환받음
print(value1)

value2 = add(4, 5) #9를 반환
print(value2)

# 도형의 면적을 계산하는 함수 정의와 사용
def square(w, h):
    return w * h

def triangle(b, h):
    return (b * h) / 2

print("사각형 면적:", square(5, 4))  # 사각형 면적: 20
print("삼각형 면적:", triangle(5, 4))  # 삼각형 면적: 10.0

# 리스트를 매개변수로 전달하는 함수 정의
# 리스트의 합계를 계산하는 함수
def calc_sum(numbers):
    total = 0
    for item in numbers:
        total += item
    return total

# 리스트의 평균을 계산하는 함수
def calc_avg(numbers):
    sum_val = calc_sum(numbers) #다른 함수를 호출
    return sum_val / len(numbers) # 평균 = 합계 / 개수

# 메인 영역 
num_list = [1, 2, 3, 4, 5]
print("리스트의 합:", calc_sum(num_list)) #함수 호출
print("리스트의 평균:", calc_avg(num_list))
