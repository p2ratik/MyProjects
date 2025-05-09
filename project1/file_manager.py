import os
import shutil
list_off_files=os.listdir(".")
def file_ext(x):
    y=x.split(".")
    return y[1]
def file_checker(name):
    if(os.path.isfile(name) ):
        return True
    else:
        return False      
list_of_only_files=list(filter(file_checker,list_off_files)) #Returns only the file that are files and no directory
list_of_filextension=list(map(file_ext,list_of_only_files)) #Retunr st the extention /type of files
set1=set(list_of_filextension) #Set of file extensions
for ext in set1:
     if(os.path.isdir(ext)): #Checks whether the directitory of the file extension already exists or not
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
           

    
       



        

    
    


       

  
     
          

    



  