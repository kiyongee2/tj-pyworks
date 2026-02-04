# 함수 - 특정한 기능을 수행하는 코드 모음
# 인사하는 함수 정의(def 키워드 사용)
def greet():
    print("Hello, Python!!")
    
def greet2(name):
    print(f"Hello, {name}!!")
    
def get_gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan*i}")
    
# 메인 영역 - 함수 호출(사용)
greet()
greet2("명제")
greet2("선화")
    
# 구구단 함수 호출
get_gugudan(8)














