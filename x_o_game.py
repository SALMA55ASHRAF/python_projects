import math 
import random
l=['x','o']
player1=""
player2=""
matrx=[['-','-','-'],['-','-','-'],['-','-','-']]
l2=[]
l3=[]
c=0
u1=input("choose the char you want to play with player1 :").lower()
u2=input("choose the char you want to play with player2 :").lower()
for sublist in matrx:
    print(*sublist)
while(c<5):
    player1=input("enter the posstion you want to play in :")
    c+=1
    if c<5:
       player2=input("enter the posstion you want to play in :")
    user=player1.split(' ')
    for i in user[:]:
        i=int(i)
        l2.append(i)
    user2=player2.split(' ')
    for i in user2[:]:
        i=int(i)
        l3.append(i)
    matrx[l2[0]][l2[1]]=u1
    matrx[l3[0]][l3[1]]=u2
    for sublist in matrx:
       print(*sublist)
    user=''
    user2=""
    l2.clear()
    l3.clear()
if matrx[0][0]==matrx[1][1]==matrx[2][2]==u1:
    print(f'player {u1} wins')
elif matrx[0][2]==matrx[1][1]==matrx[2][0]==u1:
    print(f'player {u1} wins')
elif matrx[0][2]==matrx[0][1]==matrx[0][0]==u1:
    print(f'player {u1} wins')
elif matrx[1][2]==matrx[1][1]==matrx[1][0]==u1:
    print(f'player {u1} wins')
elif matrx[2][2]==matrx[2][1]==matrx[2][0]==u1:
    print(f'player {u1} wins')
elif matrx[0][0]==matrx[1][0]==matrx[2][0]==u1:
    print(f'player {u1} wins')
elif matrx[0][1]==matrx[1][1]==matrx[2][1]==u1:
    print(f'player {u1} wins')
elif matrx[0][2]==matrx[1][2]==matrx[2][2]==u1:
    print(f'player {u1} wins')
elif matrx[0][0]==matrx[1][1]==matrx[2][2]==u2:
    print(f'player {u2} wins')
elif matrx[0][2]==matrx[1][1]==matrx[2][0]==u2:
    print(f'player {u2} wins')
elif matrx[0][2]==matrx[0][1]==matrx[0][0]==u2:
    print(f'player {u2} wins')
elif matrx[1][2]==matrx[1][1]==matrx[1][0]==u2:
    print(f'player {u2} wins')
elif matrx[2][2]==matrx[2][1]==matrx[2][0]==u2:
    print(f'player {u2} wins')
elif matrx[0][0]==matrx[1][0]==matrx[2][0]==u2:
    print(f'player {u2} wins')
elif matrx[0][1]==matrx[1][1]==matrx[2][1]==u2:
    print(f'player {u2} wins')
elif matrx[0][2]==matrx[1][2]==matrx[2][2]==u2:
    print(f'player {u2} wins')

else:
    print("no one wins")