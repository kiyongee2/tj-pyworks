# my_lib 패키지의 모듈을 사용
# from 패키지이름.모듈이름 import 함수
from my_lib.todos import cook, clean, Counter

print(cook("김치찌게"))
print(clean("욕실"))

# 카운터 객체 생성
c1 = Counter()
print(c1.get_count()) #1

c2 = Counter()
print(c2.get_count()) #2


# from 패키지이름 import 모듈이름
from my_lib import todos

print(todos.cook("파스타"))
print(todos.clean("거실"))


