# random 모듈 - 난수(무작위수)를 만들때 사용하는 모듈(라이브러리)
import random

# 무작위 수 추출
x = random.random() # 0.0 <= x < 1
print(x)

# 시드(seed) 설정 - 동일한 시드를 사용하면 동일한 난수 생성
random.seed(42)
print(random.random())

# 시드 초기화 - 무작위 수 추출
random.seed()
print(random.random())

# a에서 b까지 수중에 난수 생성 - randint(a, b)
num = random.randint(1, 10)
print(num)

# 동전 던지기
# 방법1 
coin = random.randint(0, 1)
if coin == 0:
    print("결과: 앞면")
else:
    print("결과: 뒷면")
    
# 방법2 - random.choice(리스트)
coin2 = random.choice(["앞면", "뒷면"])
print(f"결과: {coin2}")

# 리스트에서 여러 요소 선택 - choices(리스트, 개수)-중복허용
fruits = ["사과", "바나나", "딸기", "감", "사과"]
selected_fruits = random.choices(fruits, k=2)
print(f"선택된 과일(중복 허용): {selected_fruits}")

# sample(리스트, 개수) - 중복 비허용
selected_fruits2 = random.sample(fruits, k=2)
print(f"선택된 과일(중복 비허용): {selected_fruits2}")

# 로또 당첨번호 추첨 - 중복 비허용, 정렬
numbers = range(1, 46) # 1~45의 수 저장
lotto = random.sample(numbers, k=6)
print(f"생성된 로또 번호: {sorted(lotto)}")