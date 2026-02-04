# Dog 클래스 정의 - 클래스 변수
class Dog:
    kind = "진돗개" #클래스 변수(전역 변수)
    
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print(f"{self.name}가 짖습니다: 멍멍!")
        
# 객체(인스턴스) 생성
# 클래스 변수는 클래스 이름으로 직접 접근함
dog1 = Dog("초코")
print(f"Dog1 이름: {dog1.name}, 종류: {Dog.kind}")
dog1.bark()

dog2 = Dog("백구")
print(f"Dog2 이름: {dog2.name}, 종류: {Dog.kind}")
dog2.bark()