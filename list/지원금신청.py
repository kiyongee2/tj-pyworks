# 민생회복 지원금 신청 프로그램
# 출생연도의 끝자리를 이용
# 출생연도는 1900년부터 2006년 사이로 한다.
# birth_year = 2003
birth_year = input("출생연도를 입력하세요: ")
last_digit = birth_year[-1] #출생연도의 끝자리
# 문자열(출생연도)을 숫자로 변환
year = int(birth_year) 
if year < 1900 or year > 2006:
    print("출생연도는 1900년부터 2006년 사이여야 합니다.")
else:
    if last_digit in ['1', '6']:
        print("신청일은 월요일입니다.")
    elif last_digit in ['2', '7']:
        print("신청일은 화요일입니다.")
    elif last_digit in ['3', '8']:
        print("신청일은 수요일입니다.")
    elif last_digit in ['4', '9']:
        print("신청일은 목요일입니다.")
    elif last_digit in ['5', '0']:
        print("신청일은 금요일입니다.")
    else:
        print("신청 요일이 없습니다.")
