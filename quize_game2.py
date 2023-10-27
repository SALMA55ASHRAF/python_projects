#quiz game
score=0
d={
    'question1':{
        'question':'whats is capital of egypt ?',
        'answer':'cairo'

    },
    'question2':{
        'question':'whats is capital of germany ?',
        'answer':'barlin'

    },
    'question3':{
        'question':'whats is capital of plastine ?',
        'answer':'quods'

    }
}
for key,value in d.items():
    print(value['question'])
    answer=input("Answer ? ").lower()
    if answer==value['answer'].lower():
        print('correct ')
        score+=1
        print(f"your score is {score}")
        print("")
        print("")
    else:
        print("wrong! sorry ")
        print(f"the correct answer is {value['answer']}")
        print(f"your score is {score}")
        print("")
        print("")
print(f"you got {score} out of 3 questions ")
print(f"your perctange is {score/7*100}%")



    
    
    