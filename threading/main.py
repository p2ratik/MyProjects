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
    
    def __init__(self,i_t):
        self.i_t=i_t
       
    def order(self):
         
        x=len(self.item_code)
        for i in range (x):
            if(self.item_code[i]==self.i_t):
                #    print(f"The order no is :{self.i_t}\nThe name is :{self.name_pizza[i]}\nand the price is:{self.price[i]} ")
                   self.index=i
                   break
            else:
                   pass
        return self.index   

    def user_info(self):
         print("Your order will be ready in 1 minute")
         time.sleep(10)
         print(f"Your order is ready") 
         print(f"The order no is :{self.i_t}\nThe name is :{self.name_pizza[self.index]}\nand the amount payable is:{self.price[self.index]} ")
while True:
     z = input("Enter pizza name to order (or 'exit' to quit): ")
     ob1=Piza(z)
     if(z=='exit'):
          break
     baking_thread = threading.Thread(target=ob1.user_info)
     baking_thread.start()
     ob1.order()
     

          

              
         
         
              
        

           
       



    










   
    


