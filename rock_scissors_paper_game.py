# rock ,scissors and paper game 
import random
def play():
    l=['rock','scissor','paper']
    while(True):
        computer_as_player=random.choice(l)
        print(computer_as_player)
        user=input("enter rock , paper or scissors : ").lower()
        if (user not in ['rock','scissor','paper']):
            print("pls enter one of choices ")
            continue
        if user==computer_as_player:
                print('you both win yaay ')
        elif user=='paper' and computer_as_player in ['rock','scissor']:
                print('you lose try again ')
        elif user=='scissor' and computer_as_player =='rock':
                print('you lose try agin ')
        else:
                print('you win yaaaay ')
                break
play()