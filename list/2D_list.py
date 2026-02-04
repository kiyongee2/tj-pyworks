# 이차원 리스트 - 행과 열로 이루어진 리스트
# 리스트 생성
matrix = [
    [1, 2, 3],  #1행
    [4, 5, 6]   #2행
]

# 출력
print(matrix) #[[1, 2, 3], [4, 5, 6]]
print(type(matrix)) #<class 'list'>

# 특정 행 출력
print(matrix[0]) #[1, 2, 3]
print(matrix[1]) #[4, 5, 6]

# 특정 값 출력
print(matrix[0][0]) # 0행 0열, 1
print(matrix[0][1]) # 0행 1열, 2
print(matrix[1][2]) # 1행 2열, 6

# 2차원 리스트의 크기
print("행의 수:", len(matrix))
print("열의 수:", len(matrix[0]))

# 전체 값 출력
for row in matrix:  #행
    for val in row: #열 - 0행 [1, 2, 3], 1행 [4, 5, 6]
        print(val)