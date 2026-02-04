# 중첩 for문
for i in range(1, 4): #1,2,3행
    for j in range(1, 5): #1,2,3,4열
        print("가", end='')
    print()  #행 바꿈(줄 바꿈)
'''
가가가가
가가가가
가가가가
'''

# 전체 구구단(2 ~ 9단)
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print() #단이 바뀔때 마다 줄바꿈
