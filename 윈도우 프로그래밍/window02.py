# 레이아웃 - grid(행, 열)

from tkinter import *

window = Tk()
window.title("Grid 레이아웃 예제")
window.geometry("300x200")
window.option_add("*Font", ("맑은 고딕", 12)) # 전체 폰트 설정

# 레이블 생성 및 배치
Label(window, text="안녕하세요").grid(row=0, column=0, padx=10, pady=10)

# 버튼 생성 및 배치
# sticky 옵션을 사용하여 정렬 설정 (N, S, E, W)
Button(window, text="동").grid(row=0, column=1, sticky=E)
Button(window, text="서").grid(row=0, column=2, sticky=W)
Button(window, text="남").grid(row=1, column=1, sticky=S)
Button(window, text="북").grid(row=1, column=2, sticky=N)

window.mainloop()