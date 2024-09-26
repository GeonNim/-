# 문자열 조합 관련

a = "hello"
b = "world"

c = a + b
# print(c)

# 문자열 포맷팅

name = "geon"
age = 20

txt = "내 이름은 {}이고, 나이는 {}살 입니다.".format(name,age)
# print(txt)

# f-string
f_txt = f"내 이름은 {name}이고, 나이는 {age}살 입니다."
# print(f_txt)

# 문자열 이스케이프
me = "Hello, My age is \\\"20\\\" years old." # \"20\"   # \를 앞에 붙이면 문자열로 인식 시킴
# print(me)

# 문자열 개행
me2 = "hello, \nmy name is geon" # \n 을 쓴다.
# print(me2)

# 문자열 탭
me2 = "hello, \tmy name is geon" # \t 을 쓴다.
# print(me2)

# 문자열 백스페이스
me2 = "hello, \b\b\b\bmy name is geon" # \b 을 쓴다.
# print(me2)