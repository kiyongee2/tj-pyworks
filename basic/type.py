# 자료형(Data Type)
# 변수의 선언과 초기화(값을 대입)
# 함수 - print(), type()
num = 5
print(num)
print(type(num)) #<class 'int'>

rate_of_birth = 0.81
print(type(rate_of_birth)) #<class 'float'>

name_of_fruit = "사과"
print(type(name_of_fruit)) #<class 'str'>

# 논리형
b1 = True  #b1이라는 변수에 True값 저장

print(b1)
print(type(b1)) #<class 'bool'>
print(4 > 5) #False


# 자동(암묵적) 형변환
num1 = 10   #정수 
num2 = 10.3 #실수 
num3 = num1 + num2  #실수>정수 
print(num3) #20.3


#명시적 형변환 - int(), float() 사용함 
result = int(num2)
print(result)















