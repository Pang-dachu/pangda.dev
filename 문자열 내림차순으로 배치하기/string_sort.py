#프로그래머스, 문자열 내림차순으로 배치하기



s = "Zbcdefg"
print(s)
print(list(s))
print(sorted(list(s), reverse = True))
s = ''.join(sorted(list(s), reverse = True))

print(s)