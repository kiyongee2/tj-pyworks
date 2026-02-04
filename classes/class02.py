# Person 클래스 정의 및 사용
class Person:
    # 생성자 메서드(속성을 가짐)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # 소개하다(메서드)
    def introduce(self):
        print(f"안녕하세요, 저는 {self.name}이고, {self.age}세입니다.")
        
# 객체(인스턴스) 생성
"""
p1 = Person("고담덕", 39)
p1.introduce()

p2 = Person("김상희", 22)
p2.introduce()
"""

# Student 클래스 생성 및 사용
class Student:
    # 생성자 메서드
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        
    # 객체 정보 - 문자열 출력
    def __str__(self):
        return f"학생 이름: {self.name}, 학생 ID: {self.student_id}"

# 객체 생성
# student = Student("고담덕", "S10001")
# print(student)

# 객체 리스트로 생성 - 리스트 내부에 객체 저장
students = [
    Student("김상희", "S10001"),
    Student("고담덕", "S10002"),
    Student("이순신", "S10003")
]

for student in students:
    print(student)

