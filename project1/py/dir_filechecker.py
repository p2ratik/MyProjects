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
            
       
a=file_checker("Tyler.l")
print(a)   