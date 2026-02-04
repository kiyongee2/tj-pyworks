# while True - 무한반복문
# if ~ break문으로 탈출
# 1부터 5까지 출력
n = 1
while True:
    if n > 5:
        break
    print(n) # 1 2 3 4 5
    n = n + 1
    
# 1부터 10까지의 합
i = 1
total = 0
while True:
    if i > 10:
        break
    total = total + i
    print("i=", i, ", total=", total)
    i = i + 1 
print("합계:", total)
    
# 사용자에게 'y' 또는 'n'이 입력될때까지 반복
while True:
    key = input("계속하려면 'y', 종료하려면 'n'을 입력하세요: ")
    if key == 'y' or key == 'Y':
        print("계속 진행합니다.")
    elif key == 'n' or key == 'N':
        print("프로그램을 종료합니다.")
        break
    else:
        print('올바른 입력이 아닙니다. 다시 시도하세요')