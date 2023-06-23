# import datetime
# import pytz   
class Bank:
    deposits=[]
    withdrawals=[]
   
    
    def __init__(self,account_name,account_number,account_type):
       self.balance=0
       self.account_name=account_name
       self.account_number=account_number
       self.account_type=account_type 
          # print(self.value)
    def check_balance(self):
        print(self.balance)
       
    def depositing(self,amount):
        self.balance+=amount
        self.deposits.append(amount)

        
        # self.deposit_amount=deposit_amount
    def withdraw(self,amount):
        self.balance-=amount
        self.withdrawals.append(amount)

                   
bank1=Bank("loice",12378210,"personal")
bank1.depositing(300)
bank1.depositing(500)
bank1.depositing(1000)
bank1.depositing(2000)
print(bank1.balance)
bank1.withdraw(300)
bank1.withdraw(400)
bank1.withdraw(500)
print(bank1.balance)


# employee class
# creating an empty dictionary then adding the name of the employee 
# and their salary
# drivers={}
# class Workers():
#     def __init__(self,name,pay):
#         self.name=name
#         self.pay=pay
#     def proc_pay(self):
#         drivers[self.name]=self.pay
#         print(drivers)
#         # for driver,salary in drivers.items():
#         #     drivers[driver]=salary
# worker1=Workers("loice",4000)
# print(worker1.proc_pay)

# adding items to cart
class Cart:
    
    def __init__(self):
        self.items=[]
        self.prices=[]
        self.total=0
    def addtocart(self):
     while True:
        food=input("enter food to buy(q to quit): ")
        if food=="q":
            break
        else:
            price=input("enter price: ")
            self.items.append(food)
            self.prices.append(price)
    def total(self):
        for price in self.prices:
            self.total+=price
            return self.total
#items on offer
class Itemson_offer:
    def __init__(self, item_name, price,items_on_offer):
        self.item_name = item_name
        self.price = price
        self.items_on_offer =items_on_offer
        self.add_to_cart=True
    def check_offers(self):
      
        if(self.item_name in self.items_on_offer):
            self.items_on_offer[self.item_name]=self.price
            return self.price
        
                  

offer_item = Itemson_offer(["Banana","kiwi","mago"], [200,100,300],{"Banana":200,"kiwi":100,"melon":30})
print(offer_item.check_offers())




   
            
       
            

            
    
        

            

        
      