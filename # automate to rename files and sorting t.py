# automate to rename files and sorting them
import os
os.chdir('F:/project by c')
print(os.getcwd())
for f in os.listdir():
    #print(f)
    file_name,file_ext=os.path.splitext(f)
    file_title,file_number=file_name.split('-')
    file_title=file_title.strip()
    file_number=file_number.strip()[1:].zfill(2)
    new_name='{}-{}{}'.format(file_number,file_title,file_ext)
    os.rename(f,new_name)
   
    