# f-string 포멧팅

# 1. + 연산자를 사용
name = "geon"
friend = "유고"
age = 20
# print("제 이름은 " + name + "이고, 나이는 " + str(age) + "살 입니다.")

# 2. % 키워드 사용
# print("%s는 %s의 친구 입니다."%(name, friend))

# 3. format 함수 사용
# print("{}는 {}의 친구 입니다.".format(name,friend))

# 4. f-string 사용
# r을 추가하면 raw string으로 인식하여 이스케이프 문자를 무시한다. (\)
# print(fr"{name}는 \n{friend}의 친구 입니다.")
# print(f"{name}는 \n{friend}의 친구 입니다.")

# tntwkdml ruddn dustksdl rksmdgkek.
x = 10
y = 20
print(f"{x} + {y} = {x + y}")

# 변수 블록{} 내에서는 문자열의 컨트롤도 가능하다.
z = "abcdefghijklmn"
print(f"{z[:5]}")
print(f"{z.upper()[:5]}")

from datetime import date
print(f"오늘을 {date.today()} 입니다.")



