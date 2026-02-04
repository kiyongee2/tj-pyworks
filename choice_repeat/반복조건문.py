# in 명령어 - 문자열 또는 리스트(순서열)에 요소가 포함되어 있는지 확인
animals = "dog cat bird fish"

print("dog" in animals) #True
print("cat" not in animals) #False
print("bird" in animals) #True

# 챗봇(chatbot) - 규칙 기반 챗봇
'''
from datetime import datetime

now = datetime.now()
print(now) #2026-01-21 20:20:16.678210
print(f'{now.year}년')
print(f'{now.month}월')
print(f'{now.day}일')
print(f'{now.hour}시 {now.minute}분 {now.second}초')

while True:
    user_input = input("챗봇에게 질문하세요(종료는 'exit' 입력): ")
    
    if user_input == "exit":
        print("챗봇을 종료합니다.")
        break
    elif "안녕" in user_input:
        print("챗봇: 안녕하세요! 무엇을 도와드릴까요?")
    elif "이름" in user_input:
        print("챗봇: 제 이름은 챗봇입니다.")
    elif "시간" in user_input:
        now = datetime.now()
        print(f"현재 시간은 {now.hour}시 {now.minute}분입니다.")
    else:
        print("챗봇: 죄송합니다. 잘 모르겠어요")
'''
# 학점 계산 프로그램
score = int(input("점수 입력: "))
grade = ''  #공백문자로 초기화

if score >= 90 and score <= 100:
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
elif score >= 60:
  grade = 'D'
else:
  grade = 'F'
print(f"학점은 {grade}입니다.")