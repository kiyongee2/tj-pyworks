# Dog 클래스 정의 - 인스턴스 변수
class Dog:
    # 생성자 메서드
    def __init__(self, name, kind):
        self.name = name  #인스턴스 변수(지역변수)
        self.kind = kind 
        
    def bark(self):
        print(f"{self.name}가 짖습니다: 멍멍!")
        
# 객체 생성
dog1 = Dog("초코", "말티즈")
print(f"Dog1 이름: {dog1.name}, 종류: {dog1.kind}")
dog1.bark()

dog2 = Dog("백구", "진돗개")
print(f"Dog2 이름: {dog2.name}, 종류: {dog2.kind}")
dog2.bark()