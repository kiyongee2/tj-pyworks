# 요리하다
def cook(name):
    return f"{name} 요리를 합니다."

# 청소하다
def clean(place):
    return f"{place}를 청소합니다."

# 클래스형 변수 사용
class Counter:
    x = 0   #클래스 변수(값이 프로그종료시까지 유지됨)
    
    def __init__(self):
        # Counter.x = Counter.x + 1
        Counter.x += 1 #클래스 이름으로 직접 접근
    
    def get_count(self):
        return self.x

if __name__ == "__main__":    
    # 객체 생성
    c1 = Counter()
    print(c1.get_count()) #1

    c2 = Counter()
    print(c2.get_count()) #2

    c2 = Counter()
    print(c2.get_count()) #3