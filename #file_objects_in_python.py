#file_objects_in_python
f=open('F:/file_object.txt')
print("file name is: "+f.name)# to print name of file
print(f.mode)
f.close()
print(f.closed)#to check if i close the file explicity or not
with open('F:/file_object.txt','r') as f:
    print("within context manager file is in block")
    print(f.name)
    print(f.mode)
    f_content=f.read(10)
    print("this is my size of file read "+f_content)
    for line in f:
        print(line)
print(f.closed)
    