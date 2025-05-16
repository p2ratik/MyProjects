import PyPDF2
import sys
import os
  
merger = PyPDF2.PdfMerger()

list_of_all=os.listdir(".")
list1_of_dir=[z for z in list_of_all if os.path.isdir(z)]
path_original=os.getcwd()
print(path_original)

for dir in list1_of_dir:
    if(dir!="my_venv"):
     os.chdir(dir)
    else:
       continue 
    list_of_files=[]
    for file in os.listdir(os.curdir):
      if file.endswith(".pdf"):
          merger.append(file)    
    merger.write("combined.pdf")
    os.chdir(path_original)  
