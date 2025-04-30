# super keyword

""" Super is a way to access parent class methods """

""" class Phone:
    
    def __init__(self,price,brand,camera):
        print("Printing from parent class")
        self.price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smart phone printing from Smartphone class")
        # Syntax to call parent buy method
        super().buy()
    
s = SmartPhone(20000,"apple","carlzeiss") """

# if you see here first parent constructor intilasied then method of child, then it will call method of parent this is what super will do
# s.buy()





# Example 2
# How actally we use super

""" class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        print("Entering here first")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Inside smart phone constructor")


s = SmartPhone(2000,"samsung","carlzei","android",2) """

# here if you see when you call the object it goes to intilase smart phone constructor then goes to phone class again executes smartphone constructor
# also we are calling parent class attributes using super keyword
# print(s.os)




# Example 3
# using super outside class

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Printing from parent class")
        self.price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smart phone printing from Smartphone class")
        # Syntax to call parent buy method
        # super().buy()
        # calling super outside class 
    
s = SmartPhone(20000,"apple","carlzeiss")

# s.super().buy()

# If you call super outside the class it will not work will through attribute error
# Always super should be used in class generally it will be used in child class
# you cannot access parent class attributes using super, you can access only methods







        