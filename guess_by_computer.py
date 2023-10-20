import random
def guess(x):
    random_num=random.randint(1,x)
    guess=0
    guess=int(input(f"enter or guess number between 1 and {x} : "))
    while guess!=random_num:
        if guess<random_num :
            guess=int(input("your guess is small you can try again : "))
        elif guess>random_num :
            guess=int(input("your guess is high you can try again : "))
    else:
        print(f"you win you guessed {guess} correctly :) \n")
x=int(input("enter the range you want you guess number game be in : "))
guess(x)

            
    