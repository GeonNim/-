# 1. 입력 문자를 받는다. (c or f)
unit = input("온도 단위를 입력하세요 (c: 섭씨, f: 화씨): ").lower()

# 2. 입력 문자가 c 또는  f가 아니면 둘 중 하나만 입력하라고 출력한다.
if unit not in ['c', 'f']:
    print("c 또는 f 중 하나를 입력하세요.")
    exit()

# 3. 온도를 입력 받는다. (초기화 변수가 필요함)
c_or_f = ""
temp = input("온도를 입력해 주세요: ")

# 4. 입력 받은 온도가 숫자인지 확인하고, 아니라면 숫자를 입력하라고 출력한다.
try:
    temp = float(temp)
except ValueError:
    print(f"{temp}은 문자 입니다. 숫자를 입력해야 합니다.")
    exit()

# 5. 입력 받은 문자가 c 이면 화씨로 변환하고, f 이면 섭씨로 변환한다.
if unit == "c":
    c_or_f = "화씨"
    temp = (temp * 1.8) + 32
elif unit == "f":
    c_or_f = "섭씨"
    temp = (temp -32) / 1.8

# 6. 변환된 온도를 출력한다.

print(f"입력하신 변환 온도는 {c_or_f} {temp}도 입니다.")

# 아래로 해도 됨
# def temperature_converter():
#     while True:
#         unit = input("온도 단위를 입력하세요 (c: 섭씨, f: 화씨): ")

#         if unit not in ['c', 'f']:
#             print("c 또는 f 중 하나를 입력하세요.")
#             continue

#         temperature = input("변환할 온도를 입력하세요: ")

#         try:
#             temperature = float(temperature)
#         except ValueError:
#             print("숫자를 입력해야 합니다.")
#             continue

#         if unit == 'c':
#             converted_temperature = (temperature * 1.8) + 32 
#             print(f"섭씨 {temperature}도는 화씨 {converted_temperature}도입니다.")
#             exit()
#         elif unit == 'f':
#             converted_temperature = (temperature - 32) / 1.8
#             print(f"화씨 {temperature}도는 섭씨 {converted_temperature}도입니다.")
#             exit()
# temperature_converter()