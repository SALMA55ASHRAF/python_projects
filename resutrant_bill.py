import random 
people=[]
n=()
n=input("enter name of people separted by comma : ")
s=""
x=len(n)
l=n.split(",")
print(l)
for i in range(len(n)):
    if n[i] !=",":
        s+=n[i]
    else:
        people.append(s)
        s=""
   
people.append(s)
y=len(people)
print(y)

print(people[random.randint(0,y-1)]+" will pay the bill")
# or 
print(random.choice(people)+" will pay the bill")

        

