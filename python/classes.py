class Car:
    def __init__(self, max_speed,speed_unit):
        self.max_speed  = max_speed
        self.speed_unit = speed_unit
    def __str__(self):
        return "Car with the maximum speed of " + str(self.max_speed) + " " + str(self.speed_unit)  

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed
    def print(self):
        print("Car with the maximum speed of " + str(self.max_speed) + " knots.")             

class Item:
    def __init__(self,na:str,pr:int):
        self.name  = str(na)
        self.price = int(pr)

class ShoppingCart:
    def __init__(self):
        self.cart = []
    def add(self,item):
        self.cart.append(item)
    def total(self):
        prices = [x.price for x in self.cart]
        return sum(prices)
    def len(self):
        return len(self.cart)

banana = Item('banana',10)
banana.name
    
cart = ShoppingCart()          
cart.add(banana)      
cart.total()

