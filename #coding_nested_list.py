#coding_nested_list
nested_list=[[1,1,1],
             [1,1,1],
             [1,1,1]]
row=int(input("enter your pos for rows  : "))
col=int(input("enter the pos for col: "))
nested_list[row-1][col-1]="hidden my money"
for i in nested_list:
    print(*i)