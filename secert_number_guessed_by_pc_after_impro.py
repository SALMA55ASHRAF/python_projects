#secert_number_guessed_by_pc_after_improve
import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        guess=random.randint(low,high)
        feedback=input(f'Is {guess} too low (l),too high (h), or correct (c)').lower()
        if feedback=='h':
            high=guess-1
        if feedback=='l':
            low=guess+1
    print("wooow correct keep going our pc ")
x=int(input("enter range you want your pc search in strating from 1 to range you enter : "))
computer_guess(x)
        