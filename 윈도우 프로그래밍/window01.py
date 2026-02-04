# 윈도우 만들기
# CUI -> GUI
# tkinter 모듈을 사용하여 윈도우 창을 생성하는 예제
from tkinter import *

# 버튼 클릭 시 호출되는 함수 정의
def click():
    output.config(text="Hello, Tkinter!")

window = Tk()  # window 객체 생성
window.title("첫 번째 윈도우")  # 창 제목 설정
window.geometry("300x200")  # 창 크기 설정 (가로x세로)

# 레이블 만들기
# pady: 수직 패딩(위아래 여백) 설정, padx: 수평 패딩(좌우 여백) 설정
Label(window, text="안녕하세요!", font=("궁서체", 14)).pack(pady=10) 

# 버튼 만들기 - click 시 동작 설정(함수 연결) - command 인자 사용
# 주의 - click()로 쓰면 함수가 바로 호출되므로 click으로 작성(괄호생략)
Button(window, text="확인", command=click, font=("맑은 고딕", 12)).pack(pady=5)

# 클릭 후 라벨 출력
output = Label(window, text="", font=("맑은 고딕", 12))
output.pack()

window.mainloop()  # 이벤트 루프 실행, 창이 닫힐 때까지 대기