# range(시작값, 종료값, 증감값) - 실제값은 종료값-1로 출력
# list() - 리스트로 만들어주는 함수 
print(list(range(0, 5, 1))) #[0, 1, 2, 3, 4]
print(list(range(0, 5))) #[0, 1, 2, 3, 4]
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(range(0, 5, 2))) #[0, 2, 4]

# for 반복문
# 1부터 10까지 출력
for n in range(1, 11, 1): # n=1부터 10까지 순회
    print(n, end=' ') #가로로 출력
print()    

# 1부터 10까지 짝수만 출력
# 방법1
for i in range(1, 11, 1):
    if i % 2 == 0:
        print(i, end=' ') #2 4 6 8 10
print()

# 방법2
for i in range(2, 11, 2):
    print(i, end=' ') #2 4 6 8 10
print()

# 1부터 5까지 합계
total = 0  #합계 저장 변수
for n in range(1, 6):
    total = total + n
    print("n =", n, ", total =", total)

'''
n=1 , total=1
n=2 , total=3
n=3 , total=6
n=4 , total=10
n=5 , total=15
'''
print("합계:", total)

# 구구단 출력
dan = int(input("단을 입력하세요 "))
for i in range(1, 10, 1):
    # print(dan, "x", i, "=", dan*i)
    print(f"{dan} x {i} = {dan*i}")