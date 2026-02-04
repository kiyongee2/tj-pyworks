# 중첩 for문
"""
   for i in range(1, 5):  #행
       for j in range(1, 5): #열
           pass 
"""

# 5행 5열 - 별 찍기
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end='')
    print() #행(줄) 바꿈
    
"""
*
**
***
****
*****
행은 5행 변화없고, 열이 1개 증가      
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end='')
    print() #행(줄) 바꿈
'''
i=1(1행) 
  j=1, *
  j=2  종료
i=2
  j=1   *
  j=2   **
  j=3  종료
i=3
  j=1   *
  j=2   **
  j=3   ***
  j=4  종료
i=3
- 생략
'''
for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end='')
    print() #행(줄) 바꿈

# 구구단 응용 - 곱하는 수가 단보다 작거나 같은 값 출력
for dan in range(2, 10):
    for j in range(1, dan + 1):
        print(f"{dan} x {j} = {dan * j}")
    print()
    
# 구구단 - if문 사용 : 곱하는 수가 단보다 작거나 같은 값 출력
for dan in range(2, 10):
    for j in range(1, 10):
        # if dan < j: break
        if dan >= j:
            print(f"{dan} x {j} = {dan * j}")
    print()











