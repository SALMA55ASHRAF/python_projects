#quiz game
questions=['if x=1 then x+=2 : ','if x=1 then ++x: ','the result of 2+3*6/7+10 : ']
answers=['3','2','14.57']
score=0
d=dict(zip(questions,answers))
user_answers=[]
for i in d.keys():
    x=input(i)
    user_answers.append(x)
for i in d.values():
    if i in user_answers:
        score+=1
if score==3:
    print('congraltions you win your score is 100% ')
elif score>0:
    print(f'congraltions your score is {(100*score)//3}% you can try again ')
else:
    print('sorry you loss ')
    
    
    