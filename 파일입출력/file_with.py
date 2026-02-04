# 파일 쓰기 및 읽기
# 구구단을 파일에 쓰기

"""
# 파일 열기
f = open("gugudan.txt", "w")

# 파일 쓰기
# 1개의 단 출력
dan = 8
for i in range(1, 10):
    f.write(f"{dan} x {i} = {dan*i}\n")

# 파일 종료
f.close()
"""

# 종료 구문을 사용하지 않는 방식 - close() 자동 호출
# with 파일경로 as 구문
with open("gugudan2.txt", "w") as f:
    dan = 7
    for i in range(1, 10):
        f.write(f"{dan} x {i} = {dan*i}\n")
        
# 파일 읽기
with open("gugudan2.txt", "r") as f:
    content = f.read()
    print(content)