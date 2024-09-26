# 정규표현식(Regular Expression)은 문자열을 처리하는 방법 중 하나로 특정한 조건의 문자를 검색하거나치환하는 처리를 할 수 있게 하는 수단이다.

import re

# 시작과 끝
a = "I live in Korea, Incheon 13"
b = re.search("^I.*13$",a) # I로 시작하고 13으로 끝나는 문자열
# print(b)
# print(type(b))

# if b:
#     print("있습니다. 매칭되었습니다.")
# else:
#     print("없습니다. 매칭되지 않았습니다.")

# findall() : 매칭되는 모든 문자열을 리스트로 반환
# search() : 매칭되는 첫번째 문자열을 반환
# split() : 매칭되는 문자열을 기준으로 문자열을 나누어 리스트로 반환

c = re.findall("[a-dA-Z0-9]", a) # a부터 d까지의 문자열을 찾아 리스트로 반환 
# print(c)

d = re.findall(r"\d", a)  # 숫자만 검색(digits)
# print(d)

e = re.findall("K...a", a) # K로 시작하고 a로 끝나는 5글자
# print(e)

f = re.findall("K.*a", a) # K로 시작하고 a로 끝나는 모든 문자열 : 없거나 하나 이상
# print(f)

g = re.findall("Kore.+a",a) # Kore로 시작하고 a 사이에 어떤 문자가 1개 이상 있는 문자 : 하나 또는 그 이상
# print(g)

h = re.findall("Kore.?a", a) # Kore로 시작하고 a 사이에 어떤 문자가 없거나 하나 있는 문자 검색 : 없거나 하나
# print(h)

i = re.findall("K.{3}a", a) # K로 시작학소 a로 끝나며, 중간에 3글자가 있는 문자열
# print(i)

j = re.findall("live|Korea", a) # live 또는 Korea가 있는 문자열
# print(j)