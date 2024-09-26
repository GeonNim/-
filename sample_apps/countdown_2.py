import time

my_time = input("초 단위 시간을 입력해 주세요: ")

try :
    my_time = int(my_time)
except ValueError:
    print("숫자만 입력해주세요")
    exit()

# for x in reversed(range(0,my_time)): 10입력시 - 9 8 7 ...
for x in range(my_time, 0, -1): # 10입력시 - 10 9 8 7 ...
    seconds = x % 60
    minutes = (x // 60) % 60
    # :02d는 2자리 숫자로 표현하되, 1자리는 앞에 0이 붙는다.
    print(f"{minutes:02d} : {seconds:02d}")
    time.sleep(1)

print("시간이 다 되었습니다.")
