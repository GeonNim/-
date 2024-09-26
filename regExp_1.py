# special sequences : \ 문자 사용
import re

a = "geon lives in Korea, Incheon 13"

b = re.findall(r"\Ageon", a) # 문자열의 시작이 geon인 문자열
# print(b)

c = re.findall(r"geon\B", a) # geon 문자열이 뒤에 오지 않는 문자열
# print(c)

d = re.findall(r"\Bgeon", a) # geon 문자열이 앞에 오지 않는 문자열
# print(d)

e = re.findall(r"\bgeon", a) # geon 문자열이 단어의 시작에 오면 매칭
# print(e)

f = re.findall(r"\d", a) # 숫자가 있는 문자열
# print(f)

g = re.findall(r"\D", a) # 숫자가 아닌 문자열 : 공백, 특수문자 포함
# print(g)

h = re.findall(r"\s", a) # 공백 문자열
# print(h)

i = re.findall(r"\w", a) # 문자와 숫자
# print(i)

j = re.findall(r"13$", a) # 문자열 문장의 끝과 매칭
# print(j)