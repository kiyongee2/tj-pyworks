# 예외 처리
"""
   문법적인 오류는 없지만 실행될때 에러가 발생하는 것을 말한다.
   처리 방법 : try ~ except 구문을 사용한다. 
"""
# 여러가지 예외발생 예제
# print('2' + 3) #TypeError

# print(4 / 0) #ZeroDivisionError

# calculation = 10 + number #NameError (변수의 값 할당 안됨)

try:
   print('2' + 3)
except TypeError:
    print("TypeError 예외가 발생했습니다.") 
    
try:
    print(4 / 0)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
    
try:
    calculation = 10 + number
except NameError:
    print("변수가 정의되지 않았습니다.")

# 숫자를 입력할 곳에 문자를 입력한 경우 처리
'''
try:
   예외가 발생할 수 있는 구문
except:
   예외 처리 메시지
'''
try:
    x = int(input("숫자를 입력하세요: "))
    print(f"입력한 숫자는 {x}입니다.")
except ValueError:
    print("유효한 숫자를 입력하세요!")