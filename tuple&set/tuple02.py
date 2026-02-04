# 점수 저장
# 점수 리스트에 튜플로 저장
scores = [] #빈 리스트 생성

# 점수 저장
scores.append((80,))
scores.append((70,))
scores.append((90,))

# 점수 조회
print(scores) #[(80,), (70,), (90,)]

# 과목 리스트 생성 : 과목이름, 점수
subjects= []

# 과목 저장
subjects.append(("국어", 90))
subjects.append(("수학", 80))

# 과목 조회
print(subjects) #[('국어', 90), ('수학', 80)]
print(subjects[0]) #('국어', 90)
print(subjects[1]) #("수학", 80)

# 특정 요소 조회
print(subjects[0][0]) #국어
print(subjects[0][1]) #90
print(subjects[1][0]) #수학
print(subjects[1][1]) #80

# 전체 조회(for)
for row in subjects:
    print(row)



