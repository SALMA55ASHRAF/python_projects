#make_small_program_that_write_in_afile_in_format_of_csv
import csv 
l2=[]
l=[['name','age','major']]
i=1
while(i):
    n=input("ENTER your name: ")
    a=input("enter your age: ")
    m=input("enter your major: ")
    e=int(input("if you want exit enter 0:"))
    if e==0:
        i=0
    else:
        i=1
    l2=[n,a,m]
    l.append(l2)

with open('F:/myFirst_try_to_append_in_afile.csv','w')as f:
    csv_writer=csv.writer(f,delimiter=',')
    for line in l:
         csv_writer.writerow(line)
    