# 컴퓨터 용어 사전 2.0

from tkinter import *

# 딕셔너리 자료 생성
# key는 대문자로 통일

dic = {
    "CPU": "중앙 처리 장치(Central Processing Unit)의 약자로, 컴퓨터의 두뇌에 해당하는 핵심 부품입니다. 명령어를 해석하고 실행하는 역할을 합니다.",
    "RAM": "임의 접근 메모리(Random Access Memory)의 약자로, 컴퓨터가 작업을 수행하는 동안 데이터를 일시적으로 저장하는 메모리입니다. 전원이 꺼지면 데이터가 사라집니다.",
    "HDD": "하드 디스크 드라이브(Hard Disk Drive)의 약자로, 데이터를 영구적으로 저장하는 장치입니다. 회전하는 디스크에 데이터를 기록하고 읽어들입니다.",
    "SSD": "솔리드 스테이트 드라이브(Solid State Drive)의 약자로, 플래시 메모리를 사용하여 데이터를 저장하는 장치입니다. HDD보다 빠른 속도와 내구성을 제공합니다.",
}

# 검색 함수 정의

def search():
    word = entry_search.get().strip()  # 입력 상자에서 단어 가져오기(공백제거)
    if not word:  # 단어가 비어있으면
        output.delete(1.0, END)
        output.insert(END, "검색어를 입력하세요.")
        return

    key = word.upper()
    if key in dic:
        output.delete(1.0, END)  # 이전 내용 삭제(1-첫째줄, 0-첫째문자)
        output.insert(END, dic[key])  # 뜻 출력
    else:
        output.delete(1.0, END)
        output.insert(END, "사전에 없는 용어입니다.")

# 등록 함수 정의

def register_term():
    term = entry_term.get().strip()
    meaning = entry_meaning.get().strip()

    if not term or not meaning:
        output.delete(1.0, END)
        output.insert(END, "용어와 설명을 모두 입력하세요.")
        return

    key = term.upper()
    dic[key] = meaning
    output.delete(1.0, END)
    output.insert(END, f"'{key}' 용어가 등록되었습니다.")

    entry_term.delete(0, END)
    entry_meaning.delete(0, END)

# 메인 윈도우 생성
window = Tk()
window.title("컴퓨터 용어 사전 2.0")

# 검색어 입력 레이블과 엔트리(입력상자- 한줄)
Label(window, text="검색할 용어:") \
.grid(row=0, column=0, sticky=W, padx=10, pady=5)

entry_search = Entry(window, width=30)
entry_search.grid(row=1, column=0, sticky=W, padx=10, pady=5)

# 검색 버튼
Button(window, text="검색", command=search) \
.grid(row=1, column=1, sticky=W, padx=10, pady=5)

# 등록 영역
Label(window, text="새 용어:") \
.grid(row=2, column=0, sticky=W, padx=10, pady=5)

entry_term = Entry(window, width=30)
entry_term.grid(row=3, column=0, sticky=W, padx=10, pady=5)

Label(window, text="설명:") \
.grid(row=4, column=0, sticky=W, padx=10, pady=5)

entry_meaning = Entry(window, width=50)
entry_meaning.grid(row=5, column=0, columnspan=2, sticky=W, padx=10, pady=5)

Button(window, text="등록", command=register_term) \
.grid(row=3, column=1, sticky=W, padx=10, pady=5)

# 결과 출력 텍스트(여러줄)
output = Text(window, width=60, height=10)
output.grid(row=6, column=0, columnspan=2, sticky=W, padx=10, pady=5)

window.mainloop()
