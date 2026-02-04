# 인스턴스 변수를 사용한 클래스
class Counter:
    def __init__(self):
        self.x = 0  #인스턴스형 변수
        self.x = self.x + 1
        
    def get_count(self):
        return self.x
  
# 객체(인스턴스) 생성  
c1 = Counter()
print(c1.get_count()) #1

c2 = Counter()
print(c2.get_count()) #1

c3 = Counter()
print(c3.get_count()) #1
        