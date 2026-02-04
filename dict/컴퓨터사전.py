
import os

# 컴퓨터 용어 사전 구현
print("♠ 컴퓨터 용어 사전 ♠")

dic = {
    "CPU": "컴퓨터의 중앙처리 장치",
    "RAM": "임의 접근 메모리",
    "이진수": "0과 1로 이루어진 수의 체계",
    "알고리즘": "문제를 해결하기 위한 절차나 방법"
}

while True:
    # word가 key이다.
    word = input("검색할 용어를 입력하세요(종료: q or Q): ")
    if word == 'q' or word == 'Q':
        print("컴퓨터 사전을 종료합니다.")
        break
    # dic 검색
    definition = dic.get(word)
    if definition: #definition is True 생략됨
        print(f"{word}: {definition}")
    else:
        print(f"{word}는 사전에 없습니다.")

os.system("pause")  #exe파일에서 창꺼짐 방지