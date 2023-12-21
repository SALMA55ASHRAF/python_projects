import random # module
game={'Head':1,
      'Tail':0}
print("welcome to my Head-Tail game")
print('_'*25)
print("Head or Tail ?!")
input1='yes'
while(input1=='yes'):
 player=input("hey enter your guess : ").capitalize()
 if player.capitalize() not in ('Head','Tail'):
     player=input("wrong you enter the wrong choice enter your guess again  : ") 
 true_of_coin=random.randint(0,1)
 print(true_of_coin)
 if player=='Head':
    player=1
 else:
    player=0
 if true_of_coin==player:
    print("you win yohoooooooo ")
 else:
    print("you lose anoanoanonono ")
 input1=input("want to try again : ").lower()
 if input1 not in ('yes','no'):
    input1=input("want to try again enter the right choice if YES or NO : ")
print("you exit the game thank you for playing see you later :) ")



