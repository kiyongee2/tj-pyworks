# 매개변수 - 함수의 괄호안에 포함되는 변수이다.
# 기본 매개변수(default parameter)

def take_bus(fare=1500):
    print(f"버스 요금은 {fare}원입니다.")
    
take_bus() #버스 요금은 1500원입니다.
take_bus(1700) #버스 요금은 1700원입니다.