import os
import shutil
list_off_files=os.listdir(".")
def file_ext(x):
    y=x.split(".")
    return y[1]
def file_checker(name):
    flag=0
    for ch in name:
        if(ch=='.'):
            flag=1
            break
        else:
            flag=0
    if(flag==0):
        return False
    else:
        return True                
list_of_only_files=list(filter(file_checker,list_off_files)) #Returns only the file that are files and no directory
list_of_filextension=list(map(file_ext,list_of_only_files)) #Retunr st the extention /type of files
print(list_of_filextension)
set1=set(list_of_filextension)
set2=set(list_off_files)
print(set1)
for ext in set1:
     if(os.path.isdir(ext)):
         print(" ")
     else:
         os.mkdir(ext)    

for files in list_of_only_files:
     x=files.split(".")
     a=x[1] 
     if(a=="py"):
         print(" ")   
     else:
      shutil.move(files,f"{a}/")
           

    
       



        

    
    


       

  
     
          

    



  