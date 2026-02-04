# 입력 처리 - input()
# 여러줄 주석 - """ ~ """(홑따옴표, 쌍따옴표 모두 가능)
"""
print("문자입력: ")
char = input()
print(char)
"""

'''
char = input("문자입력: ")
print(char)
'''

"""
num = input("정수 입력: ")
num = int(num) #int(문자) -> 숫자로 변환하는 함수 

print(type(num))
print(num + 1)
"""

# 입력받은 실수는 문자형이므로 숫자형을 변환
# 함수 - float(문자) -> 실수로 변환함 
# 몸무게를 입력받아서 2로 나누기
# 방법 1
'''
weight = input("몸무게 입력: ")
weight = float(weight)
print(weight/2)
'''

# 방법 2
'''
weight = float(input("몸무게 입력: "))
print(weight/2)
'''

# 나이 계산 프로그램
# 나이(age) = 현재연도 - 태어난연도(birth_year) + 1
birth_year = int(input("태어난 해를 입력하세요: "))

age = 2026 - birth_year + 1
print("나이는", age, "세입니다")
print(f"나이는 {age}세입니다.") #변수는 중괄호({})로 감싼다.



















