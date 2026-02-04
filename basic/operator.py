# 연산자
# 산술 연산 
n1 = 10 #대입 연산자 - '='
n2 = 4

print("n1 + n2 =", n1 + n2) #14
print("n1 - n2 =", n1 - n2) #6
print("n1 * n2 =", n1 * n2) #40
print("n1 / n2 =", n1 / n2) #2.5
print("n1 // n2 =", n1 // n2) #2 - 몫
print("n1 % n2 =", n1 % n2) #2 - 나머지
print("n1 ** n2 =", n1 ** n2) #10000 - 거듭제곱

#비교 연산자 - 조건 1개 
x = 10
y = -10

print(x > 0) # True
print(y > 0) # False
print()

print(x > y) #True
print(x < y) #False
print()

print(x == 10) #True '==' 동등 연산자 
print(x == y) #False
print(x is y) #False

print(x != y) #True
print(x is not y) #True
print()

# 논리 연산자 - 조건이 2개 이상,
# A and B (A와 B가 모두 True일때만 True)
# A or B (A와 B가 둘중 1개만 True일때 True)
# not A, not B (A가 True이면 False)
print(x > 0 and y > 0) # True and False -> False
print(x > 0 or y > 0) # True and False -> True
print(not (y > 0)) # not False -> True

# 문자열 연산
head = "Good"
tail = " Job!"
print(head + tail) #Good Job!
print(head * 3) #GoodGoodGood


# num을 2로 나눈 나머지
num = 11

print(num % 2 == 0) #False
print(num % 2 == 1) #True
print(num % 2 != 0) #True
print(num % 2 != 1) #False

# 실습문제 1 - 몫과 나머지 계산하기
bread = 30
people = 4
share = bread // people
remain = bread % people

print("몫:", share , ", 남은 빵:", remain)






























