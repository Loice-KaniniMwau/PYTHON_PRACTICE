# oop in python
class Robot():
    def __init__(self,name ,age ,weight) :
        self.name=name
        self.age=age
        self.weight=weight
    def introduce_self(self):
        print("hello" + self.name)
r1=Robot("loice",30,5.6)
class Kettle(object):
    def __init__(self,make ,price):
        self.make=make
        self.price=price
        self.on=False
    def switch_on(self):
        self.on=True

kenwood=Kettle("Kenwood",8.5)
print(kenwood.make)
print(kenwood.make)
# changing the values
kenwood.price=12.5
print(kenwood.price)
hamilton=Kettle("Hamilton",14.55)
# specify attributes
        
class Bank(object):
    accounts={}
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
        Bank.accounts[self.name]=self.amount

    def deposit(self,amount):
        Bank.accounts[self.name]= self.amount+amount
        print(f"you account has been credited {amount}")
    def withdraw(self,amount):
        Bank.accounts[self.name]-=amount
        print(f"your account has been debitted {amount}")
    def transfer(self,receiver,amount):
        self.withdraw(amount)
        receiver.deposit(amount)
        print(f"you have transferred {amount} to {receiver}")
customer1=Bank("loice",5000)
customer2=Bank("mary",3000)
customer3=Bank("faith",4000)
customer1.deposit(2000)
customer2.deposit(3000)
customer3.deposit(200)
print(Bank.accounts)
customer1.withdraw(200)

print(Bank.accounts)
customer1.transfer(customer2,2000)
print(Bank.accounts)

# add to cart
foods=[]
prices=[]
total=0
while True:
    food=input(f"please enter the  (q to quit):")
    if (food=="q"):
        break
    else:
        price=float(input(f"please enter price: "))
        foods.append(food)
        prices.append(price)
    
for food in foods:
    foods.append(food)
for price in prices:
    total+=price

print(total)



    