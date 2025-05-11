import re
import time 
import threading
class Piza:
    with open("pizza.txt","r") as file:
          pattern1=r"100+[1-9]"
          pattern2=r"Rs[=:]?(\d+)"
          pattern3=r'\d+\s+([A-Za-z ]+?)::'
          content=file.read()
          print(content)
          item_code=re.findall(pattern1,content)
          price=re.findall(pattern2,content)
          name_pizza=re.findall(pattern3,content) 
          index=0 
          order_no=0
         
    def __init__(self,i_t,quantity):
        self.i_t=i_t
        self.quantity=quantity   
    def order(self):      
        x=len(self.item_code)
        for i in range (x):
            if(self.item_code[i]==self.i_t):
                   self.index=i
                   break
            else:
                   self.index=-1
        return self.index   
    def user_info(self):
         if(self.index>=0):
            self.order_no=self.order_no+1
            print("Your order will be ready in 1 minute")
            time.sleep(10)
            print("-------ORDER------")
            print(f"order no {Piza.order_no} is ready ::") 
            cost=float(self.price[self.index])*float(self.quantity)
            print(f"The pizza no is :{self.i_t}\nThe name is :{self.   name_pizza[self.index]}\nand the amount payable is:{cost} ")
         else:
              print("Thats a wrong input try again !! ")
    @classmethod          
    def order_no_update(cls):
         cls.order_no+=1
         return cls.order_no         
i=0
while True:
     
     Piza.order_no=Piza.order_no+1
     name_customer=input("Please Enter your name : ")
     ph_no=input("Please Enter your contact number: ")
     z = input("Enter pizza code to order (or 'exit' to quit): ")
     if(z=='exit'):
          break
     y=input("Enter the quantity of your pizza : ")
     ob1=Piza(z,y)
     #ob1.order_no_update()
     with open("data_customer.txt","a") as data:
          data.write(f"Order no {Piza.order_no}: Name :{name_customer} Contact number : {ph_no}\n")   
     ob1.order()
     baking_thread = threading.Thread(target=ob1.user_info)  
     baking_thread.start()
     baking_thread.join()
     
     
     

          

              
         
         
              
        

           
       



    










   
    


