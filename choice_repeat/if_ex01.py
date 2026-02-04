# 조건문 - if문
# 조건식이 True일때 실행함
# 들여쓰기(인덴트) - 4칸
# 나이가 만 19세 이상이면 "성인", 아니면 "미성년자"
age = 21

'''
if age < 20:
    print("미성년자입니다.")
'''

# if ~ else문
if age < 20:
    print("미성년자입니다.")
else: #elif age >= 20:
    print("성인입니다.")
    
print(f"나이는 {age}세입니다.")


# if ~ 내부 if문
num = 12

if num > 10:
    if num < 20:
        print("10보다 크고 20보다 작은 수입니다.")
    else:
        print("20 이상의 수입니다.")
else:
    print("10 이하의 수입니다.")

# 다중 if문 -> if ~ elif ~ else
print("=== 놀이 공원 입장료 계산 ===")
age = int(input("나이를 입력하세요: "))
fee = 0 #입장료는 0으로 초기화 해줌

if age < 14:  #30 < 14
    fee = 1000
    print("어린이 요금이 적용됩니다.")
elif age < 19:
    fee = 2000
    print("청소년 요금이 적용됩니다.")
elif age < 65:
    fee = 3000
    print("성인 요금이 적용됩니다.")
else:
    fee = 1500
    print("경로 우대 요금이 적용됩니다.")    

print(f"입장료는 {fee}원입니다.")










