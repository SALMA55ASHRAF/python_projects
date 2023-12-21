# my first try for automation 
import os 
os.chdir('C:/Users/DELL/Downloads/salmaashrafinfo')
print(os.getcwd())
for files in os.listdir():
    file_name,file_ext=os.path.splitext(files)
    #print(file_name,file_ext)
    file_name=file_name.split('-')
    file_order=file_name[1]
    file_name=file_name[0]
    new_format='{}-{}{}'.format(file_order,file_name,file_ext)
    os.rename(files,new_format)