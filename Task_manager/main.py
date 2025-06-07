
class Task:
    list1=[]
    def __init__(self):
        pass
    def add_task(self):
       self.task=input("Enter your task:: ")
       self.date=input("Enter date in the form of (YYYY-MM-DD):: ")
       self.dict1={"task":self.task,"Due Date":self.date,"Status":"Pending"}
       self.list1.append(self.dict1)
       print("Task Added successfully")

    def complete_task(self,task_no):  
        self.list1[task_no]["Status"]="Complete"
        print(f"{task_no+1} is completed :")
    
    def show(self):
        print("----:::Your Tasks are :::----\n")
        for d in self.list1:
            print("Task:",d["task"])
            print("Due Date:",d["Due Date"])
            print("Status:",d["Status"])
            print("--------------------")
    def delete_task(self,task_no):
        del self.list1[task_no-1]
        print("Your Task has been deleted sucessfully :::: ")
def main():   
   pointer=True  
   print("Welcome to task Manager ")
   print("What would you like to do?")     
   var='''
   1. View Tasks
   2. Add a Task
   3. Mark Task as Complet   
   4. Delete a Task
   5. Exit
   '''
   ob=Task()
   print(var)
   while pointer:
        x=int(input("Enter your choices::"))   
        if(x==1):
            ob.show()
        elif(x==2):
             ob.add_task()
        elif(x==3):
             task_no=int(input("Enter the task number to mark as complete: "))      
             ob.complete_task(task_no-1) 
        elif(x==4):
            task_no=int(input("Enter the task number to be deleted: "))    
            ob.delete_task(task_no)
        elif(x==5):
             pointer=False
             print("Thank you for using Task Manager:::")    
        else:
             print("Enter correct choice :")
             break        
if __name__=="__main__":
    main()


    


