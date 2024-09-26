# type castion : 타입 변환

# 1. str : 문자열
x = "hello"

# 2. int : 정수, float : 실수, complex : 복소수
y= 10
# print(type(y))

z = 10.5
# print(type(z))


a = 5j
# print(type(a))

# 3. 집합 자료형 : list, tuple, dict, set

## list
b=['apple','banana','cherry']
# print(type(b))

## tuple
c = ('포도','수박','참외')
# print(type(c))

## dict
d= {"name": "geon", "age": 30}
# print(type(d))

## set : 순서가 없다.
e = {'포도','수박','참외'}
e.add('딸기')
# print(type(e))
# print(e)

# 4. bool: True, False
f = True
# print(type(f))

# 5. type castion
g = "3"
h = int(g)
i = float(g)
# print(type(g),type(h),type(i))

# 6. 여러줄 문자열 표기
## - """ 다음에 엔터를 입력하면 첫줄에 공백이 생긴다. 없애려면 """\ 를 사용한다.
j= """\
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\
"""

print(j)