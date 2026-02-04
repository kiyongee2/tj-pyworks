# 리스트의 주요 함수
# append() - 요소 추가
a1 = [1, 2, 3, 4, 5]
a2 = []  #빈 리스트 생성

# a1의 요소를 a2에 저장함
for item in a1:
    a2.append(item)
print("a2 =", a2)

# a3 리스트에 a1 요소중 홀수만 저장
a3 = []
for item in a1:
    if item % 2 == 1:
        a3.append(item)
print("a3 =", a3) #a3 = [1, 3, 5]

# 요소의 개수
print(len(a1)) #5
print(len(a2)) #5
print(len(a3)) #3

# 리스트의 연산 - 개수, 합계, 평균
lst = [10, 20, 30, 40]

# 요소의 개수
print(len(lst)) #4

# 요소의 합계
total = lst[0] + lst[1] + lst[2] + lst[3]
print(total) #100

total = 0  # 합계 초기화(필수)
for item in lst:
    # print(item)
    # total = total + item
    total += item
"""
   1회전 item -> 10
   2회전 item -> 20
   3회전 item -> 30
   4회전 item -> 40 
"""
print("요소의 합계:", total)

# 평균 = 합계 / 개수
average = total / len(lst)
print("요소의 평균:", average) #25.0




