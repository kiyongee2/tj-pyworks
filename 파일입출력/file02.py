# 리스트를 쓰고 읽기
carts = ["라면", "달걀", "삽겹살", "콜라"]

try:
    # 파일 열기
    f = open("c:/pyfile/carts.txt", 'w')

    # 파일 쓰기
    for item in carts:
        f.write(item + '\n')

    # 파일 종료
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
    
# 파일 읽기
try:
    f = open("c:/pyfile/carts.txt", 'r')
    
    content = f.read()
    print("파일 내용:")
    print(content)
    
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")