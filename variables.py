#  변수 : 특정한 키워드 없이 사용
x = 10
# print(x)
# print(type(x))

y = "geon"
# print(type(y))

z=3.5
# print(type(z))

# type castion : 타입 변환
a = "3"
# print(type(a))
b = int(a)
# print(b)
# print(type(b))

# print(str(3))
# print(int(3))
# print(float(3))

# 변수 이름 규칙
# 1. 숫자로 시작하는 이름 사용 불가
# 2. 특수문자는 언더바 _ 만 허용
# 3. 대소문자 구분함
# 4. 예약어 사용 불가 : if, int, else, ...
# 5. 중복단어는 언더바로 구분 : my_name, ... (권고사항)

# 변수 여러개 선언
name, age, address = "geon", 30, "shinchon"
#print(name,age,address)

# 여러개의 변수에 하나의 값 저장
x = y = z = 10
#print(x,y,z)

# list(리스트) 구조분해 할당
fruits = ['apple','banana','cherry']
a,b,c = fruits
#print(a,b,c)
#print(fruits)

# 변수 연결 - 문자열화
name = "geon"
age = 20
# print("이름: " + name + ", 나이: " + str(age))

# 전역 변수
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Pythons is " + x)

myfunc()

print("Pythons is " + x)