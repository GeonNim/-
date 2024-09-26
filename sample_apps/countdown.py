# sleep 함수 : 일정 시간동안 프로그램을 멈추는 함수

import time
# time.sleep(3)

# print('3초가 지났습니다.

# for x in reversed(range(0, 10, 2)):
#     print(x)



# print(minutes)
myTime = input("시간입력 : ")
try:
    myTime = int(myTime)
except:
    print("숫자로 입력하시오.")
    exit()

for x in reversed((range(0,myTime,1))):
    time.sleep(1)
    seconds = x % 60
    minutes = (x // 60) % 60 

    print(f" 00 : {minutes} : {seconds}")
    if seconds == 0:
        minutes -= 1
        
        
    elif minutes < 0:
        print(f" 00 : {minutes} : {seconds}")
        break
    
