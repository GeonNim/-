from hangman_words import words
import random


# words = ["apple", 'banana', 'orange', 'grape']

hangman_draw = {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\"),}




# for line in hangman_draw[5]:
#     print(line)

# 행맨 그리기 함수
def display_man(wrong_answer):
    for line in hangman_draw[wrong_answer]:
      print(line)

# 힌트 출력 함수
def display_hint(hint):
    print(" ".join(hint))

# 정답 출력 함수
def display_anser(answer):
    print(" ".join(answer))

def main():
    guessed_letters = set() # 초기화 set
    is_run = True
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_answer = 0
    # print(hint)
    while is_run:
        display_man(wrong_answer)
        display_hint(hint)
        
        # print(guessed_letters)

        guess = input("알파벳을 입력해 주세요: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 입력해 주세요.")
            continue
        
        if guess in guessed_letters:
            print("이미 입력한 알파벳 입니다.")
            continue
        guessed_letters.add(guess)
        # print(guessed_letters)
        
        # 입력한 글자가 정답에 포함되어 있는지 확인
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_answer += 1
        
        if "_" not in hint:
            print("서세수.")
            display_anser(answer)
            is_run = False
        elif wrong_answer >= len(hangman_draw) - 1:
            print("유다희.")
            display_man(wrong_answer)
            display_anser(answer)
            is_run = False

        

        

if __name__ == "__main__":
    main()