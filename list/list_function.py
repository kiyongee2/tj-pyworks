# 리스트 제공 함수
numbers = [5, 2, 9, 1, 5]

# 인덱스로 조회
print(numbers[0]) #5
print(numbers[2]) #9

# 슬라이싱(범위 조회)
print(numbers[1:4]) #[2, 9, 1]
print(numbers[:-1]) #[5, 2, 9, 1]
print(numbers[:]) #[5, 2, 9, 1, 5]

# 요소 정렬 - sort()
numbers.sort() #오름차순
print("sort 후:", numbers) #[1, 2, 5, 5, 9]

# 요소 뒤집기 - reverse()
numbers.reverse()
print("reverse 후:", numbers) #[9, 5, 5, 2, 1]

# 리스트 복사 - copy()
copied_numbers = numbers.copy()
print("copy 후:", copied_numbers) #[9, 5, 5, 2, 1]

# 요소 추가
copied_numbers.append(10)
print("10 추가후:", copied_numbers) #[9, 5, 5, 2, 1, 10]

# 여러개의 요소 추가 - extend(리스트)
# copied_numbers.append(11, 12)  #오류발생
copied_numbers.extend([11, 12])
print("10, 11 추가후:", copied_numbers) # [9, 5, 5, 2, 1, 10, 11, 12]

# 요소 삭제 - remove()
copied_numbers.remove(5)
print("5 삭제후:", copied_numbers) #[9, 5, 2, 1, 10, 11, 12]
