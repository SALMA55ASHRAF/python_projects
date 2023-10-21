# data structer in python
# 1st function
def f(lst):
    keys=set(lst)
    keys=list(keys)
    keys.sort()
    values=[]
    for i in keys:
     if i%3==0:
         values.append("this value divisible by 3")
    else:
         values.append("this value not divisible by 3")
    dictonary=dict(zip(keys,values))
    return dictonary
lst=[1,3,3,2,7]
print(f(lst))
#2nd function
def fun(lst):
    lst_as_set=set(lst) #to get unique value
    d={}
    for num in lst_as_set:
        d[num]=0 # set initial value for keys to be zero 
    for key in d:
        if (key%3==0):
            d[key]='divisble by 3'
        else:
            d[key]='not divisible by 3'
    return d
print(fun([1,3,3,2,7]))
    