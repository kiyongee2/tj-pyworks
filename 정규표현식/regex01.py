# 정규 표현식 - 문자열에서 특정 패턴을 찾거나, 검사하는 도구

import re

# 1. re.match() - 문자열의 시작부터 패턴이 일치하는지 검사

text = "korea"

pat = re.compile("[a-z]+")  # a부터 z까지의 소문자가 하나 이상 있는 패턴
mat = pat.match(text)
print(mat)  # <re.Match object; span=(0, 1), match='k'>
print(mat.group())  # k