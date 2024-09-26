
def show_balance(balance):
    print(f"현재 잔액은 {balance}원 입니다.")

def deposit():
    while True:
        amount = input("입금할 금액을 입력해 주세요 : ")

        try:
            amount = int(amount)
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue

        if amount < 0:
            print("0보다 큰 숫자를 입력해 주세요")
            return 0
        else:
            return amount

def withdraw(balance):
    while True:
        amount = input("출금할 금액을 입력해 주세요 : ")

        try:
            amount = int(amount)
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue

        if amount > balance:
            print("잔액이 부족합니다.")
            return 0
        elif amount <= 0:
            print("0보다 큰 숫자를 입력해 주세요")
            return 0
        else:
            return amount


def main():
    balance = 0
    is_run = True
    while is_run:
        print("1. 잔액보기")
        print("2. 입금하기")
        print("3. 출금하기")
        print("4. 종료하기")
    
        choice = input("1 ~ 4번 중 선택해 주세요: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_run = False
        else:
            print("1 ~ 4번 중 선택해 주세요.")
            continue
        
     
    

if __name__ == "__main__":
    main()