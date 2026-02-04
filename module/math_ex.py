# 모듈(module)
"""
# 모듈은 python 파일 하나를 의미하며 다른 python 프로그램에서
  모듈의 함수, 클래스등을 재사용할 수 있다.
  - 사용방법
    import 모듈이름
"""

# 반올림
print(round(2.54)) #3

import math

# 올림
print(math.ceil(2.14)) #3

# 내림
print(math.floor(2.54)) #2

# 제곱근
print(math.sqrt(2)) #1.4142135623730951
print(math.sqrt(16)) #4.0
print(int(math.sqrt(16))) #4 (정수로 변환)

# 원주율
print(math.pi) #3.141592653589793

# 원의 넓이 = pi * 반지름 * 반지름
radius = 4
area = math.pi * radius ** 2
print(f"원의 넓이: {area:.2f}") #소수둘째자리 출력
