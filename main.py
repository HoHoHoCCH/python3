import random
import time

showanswer = 0

print("Welcome to timeNumber")
print("How To Play")
print(
    "1. Type out the SUM of the 3 numbers within a amount seconds depending on ur level, the numbers are randomly "
    "selected depending on the level "
    "you chose.")
print("2. Try Beating MY highscore! (2 points)")
user1 = input("Begin? (Enter Anything To Continue.)")
if user1 == "showanswer.cheat":
    showanswer = 1
    print("CHEAT >> Cheat showanswer.py is activated.")

while True:
    level = int(input("Select ur level (5 is recommended)"))
    try:
        level1 = int(level * 2)
        print("Ok! Level", level, "Selected!")
        level = level * 3
        time.sleep(1)
        print("The maximum numbers shown is up to", level1)
        time.sleep(1)
        print("And the seconds allowed for each question is", level, "seconds")
        time.sleep(1)
        user1 = input("Begin? (Enter Anything To Continue.)")
        break
    except ValueError:
        print("That is NOT a NUMBER! Enter A NUMBER")
        continue

print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("GO!")
score = 0
while True:
    answer1 = 0
    num1 = random.randint(1, level1)
    num2 = random.randint(1, level1)
    num3 = random.randint(1, level1)
    final = num1 + num2 + num3
    # print(final)
    print(num1, num2, num3)
    start = time.time()
    answer = int(input(">>>"))
    end = time.time()
    elapsed = end - start

    if elapsed >= level:
        print("You used more than", level, "seconds! You LOSE!")
        tryagain = input("Press ENTER to play again!(or press n, then enter to exit)")
        if tryagain == "n":
            exit()
        else:
            exec(open('main.py').read())
    else:
        if answer == final:
            score += 1
            print("Correct! You now have", score, "points!")
            continue
        else:
            print("The Answer is WRONG! You LOSE!")
            tryagain = input("Press ENTER to play again!(or press n, then enter to exit)")
            if tryagain == "n":
                exit()
            else:
                exec(open('main.py').read())
