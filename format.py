# 문자열 포멧팅
age = 20
msg = "제 이름은 마샬이고, 나이는 {}살 입니다."
a = msg.format(age)
#print(a)

name = "건"
txt = "저는 {}이고, 나이는 {}입니다."
# {0}, {1}이 생략된 형태
b = txt.format(name, age)
# print(b)

txt = "저는 {name}이고, 나이는 {age}입니다."
b = txt.format(name = "건", age = 20)
# print(b)

# 자리수 지정 포멧팅
# 변수 앞으로 5 자리 까지 확보하고 오른쪽 정렬 초과하면 밀림
c = "저는 {:>5}마리의 닭을 기릅니다."
# print(c.format(5))
# print(c.format(50))
# print(c.format(500))
# print(c.format(500000))
# print(c.format(50000000))

# 가운데 정렬 공간 확보
d = "저는 {:^7}마리의 닭을 기릅니다."
# print(d.format(5))
# print(d.format(50))
# print(d.format(500))

# 음수 표시는 음수 표시, 양수 표시는 기호 없이 그냥 양수 표시
e = "저는 {:=6}마리의 닭을 기릅니다."
# print(e.format(-5))
# print(e.format(50))
# print(e.format(-500))

# :+ 기호를 붙일 경우 양수에도 기호를 붙이며, 음수에는 음수 기호가 붙는다.
f = "오늘의 최고 기온은 {:+}도 이고, 최저 기온은 {:+}도 입니다."
# print(f.format(10,-5))

# {:,} - cjs eksdnlfh zhaakfmf Wlrdjwnsek.
g = "저는 {:,}원을 가지고 있습니다."
# print(g.format(10000000000))

# {:.0%} - 백분률로 표시
h = "오늘의 확률은 {:.0%}입니다."
print(h.format(0.4))








