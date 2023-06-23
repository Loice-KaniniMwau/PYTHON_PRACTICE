# Cart Management system
class Cart:
    def __init__(self, item,prices,cart,total):
        self.item = item
        self.prices = prices
        self.cart = cart
        self.total = total
    
# Kijani groceries cart will enable our customers to add their 
# selected items to be added to the cart to make it easier to know what to pay for
    
    def add_to_cart(self,item):
        while True:
            item = input("Select an item (q to quit):")
            if item == "q":
                break
            else:
                price = input(f"Enter the price of {item}")
                self.cart.append(item)
                self.prices.append(price)
            for item in self.cart:
                print(item)
            for price in self.prices:
                total += price
                print(f"Your total amount is:ksh{total}")

item1=Cart("kiwi",[],[],0)
item1.add_to_cart()
print(item1.add_to_cart)