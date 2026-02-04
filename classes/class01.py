"""
# 클래스(Class) 
  - 객체(사물)의 속성과 메서드(함수)를 하나의 단위로 묶은 틀
  - 클래스는 설계도와 같으며 이를 기반으로 여러 객체를 생성할 수 있음
  - 첫글자 대문자를 사용
  - 클래스의 메서드의 매개변수는 기본 self를 사용함
"""
# 자동차 클래스 정의
class Car:
    # 속성(Attribute)
    color = "white"
    wheels = 4
    
    # 함수(메서드- method)
    def drive(self):
        print("자동차가 달리고 있습니다.")
        
# 클래스의 사용 -> 객체(인스턴스)를 생성
# 인스턴스(객체) = 클래스(생성자) -> 괄호 주의
# 객체는 변수(속성)와 함수(메서드)에 접근할 수 있음(점 연산자 사용)
car1 = Car()
print("자동차 색상 :", car1.color)
print("자동차 바퀴 개수 :", car1.wheels)
car1.drive()

# 자전거 클래스
class Bike:
    # 생성자 메서드 - 객체가 생성될때 자동으로 호출되는 특별한 메서드
    def __init__(self, color, gears):
        self.color = color
        self.gears = gears
        
    def get_info(self):
        return f"자전거 색상: {self.color}, 기어 수: {self.gears}"
        
# 객체 생성
my_bike = Bike("blue", 10) 
print(my_bike.get_info())

your_bike = Bike("black", 12)
print(your_bike.get_info())