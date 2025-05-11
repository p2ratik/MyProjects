import re
import time
import threading

class Piza:
    item_code = []
    price = []
    name_pizza = []
    order_no = 0

    @classmethod
    def load_menu(cls):
        try:
            with open("pizza.txt", "r") as file:
                content = file.read()
                print(content)
                cls.item_code = re.findall(r"100+[1-9]", content)
                cls.price = re.findall(r"Rs[=:]?(\d+)", content)
                cls.name_pizza = re.findall(r'\d+\s+([A-Za-z ]+?)::', content)
        except FileNotFoundError:
            print("Menu file not found.")
            exit()

    def __init__(self, i_t, quantity):
        self.i_t = i_t
        self.quantity = quantity
        self.index = -1

    def order(self):
        for i in range(len(Piza.item_code)):
            if Piza.item_code[i] == self.i_t:
                self.index = i
                break
        return self.index

    def user_info(self):
        if self.index >= 0:
            print("Your order will be ready in 1 minute...")
            time.sleep(10)
            Piza.order_no += 1
            cost = int(Piza.price[self.index]) * int(self.quantity)
            print(f"\n--- Order Complete ---")
            print(f"Order No: {Piza.order_no}")
            print(f"Pizza Code: {self.i_t}")
            print(f"Name: {Piza.name_pizza[self.index]}")
            print(f"Quantity: {self.quantity}")
            print(f"Total Cost: Rs {cost}")
        else:
            print("That's a wrong input. Try again!")

# Load menu once at start
Piza.load_menu()

while True:
    name_customer = input("Please Enter your name: ")
    ph_no = input("Please Enter your contact number: ")
    code = input("Enter pizza code to order (or 'exit' to quit): ")
    if code.lower() == 'exit':
        break
    quantity = input("Enter the quantity of your pizza: ")

    pizza_order = Piza(code, quantity)
    pizza_order.order()

    with open("data_customer.txt", "a") as data:
        data.write(f"Order no {Piza.order_no + 1}: Customer: {name_customer}, Contact: {ph_no}\n")

    baking_thread = threading.Thread(target=pizza_order.user_info)
    baking_thread.start()
    
     # Optional: wait for baking to complete before next input
