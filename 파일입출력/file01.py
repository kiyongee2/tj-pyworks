# 파일 입출력
# 파일에 내용 쓰기(저장)

# 파일 열기 - open(파일 경로, 모드), w-쓰기모드
# 파일 없으면 새로 생성되고, 있으면 내용이 저장된다.
try:
    f = open("c:/pyfile/file1.txt", 'w')

    # 파일 쓰기 - write(데이터)
    f.write("sky\n")  #줄바꿈 기호 - '\n'
    f.write("겨울이 한창입니다.\n")
    # f.write(100) #숫자 쓰기 불가 #TypeError
    num = 100
    f.write(f"{num}")

    # 파일 종료 - close()
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 파일 읽어오기
# 파일 열기 - r: 읽기 모드
# try ~ except 구문
try:
    f = open("c:/pyfile/file1.txt", 'r')

    # 파일 읽기 - read()
    content = f.read()
    print("파일 내용:")
    print(content)

    # 파일 종료
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
