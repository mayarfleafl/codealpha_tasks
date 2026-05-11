import random


subjects = ["math", "science", "arabic", "english", "history", "computer"]
subRan = random.choice(subjects)
n = 1
while(n <= 6):
    subject = input("Guess the word: ").strip().lower()
    if subject == subRan:
        print("Correct answer!")
        break
    elif subject != subRan:
        if(n == 6):
            print("Game over!")
            print("The correct word was:", subRan)
        else:
            print("Wrong answer, try again.")
    n += 1
