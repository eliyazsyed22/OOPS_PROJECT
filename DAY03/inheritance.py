# Inheritance


#parent class
class User:
    
    
    def __init__(self,name):
        self.name = name
        
    def login(self):
        print('login')



# child class
class Student(User):
    
    def __init__(self):
        self.roll_num = 10
        
    def enroll(self):
        print('enroll into course')


u = User('eliyaz')

s = Student()

# s.enroll()



# another example for inheritance


class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")

        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a smart phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(2000,'Apple',13)

# print(s.price)
# s.buy()



## child class with own constructor

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Another phone constructor")

        self.price = price
        self.brand = brand
        self.camera = camera

    # def buy(self):
    #     print("Buying a phone")


class SmartPhone(Phone):
    
    def __init__(self,os,ram):
        self.os = os
        self.ram = ram
        print("Inside the smart Phone constructor")


    # def buy(self):
    #     print("Buying a smart phone")


# s = SmartPhone("android",2)

# print(s.brand)


# 3 child can't access private members of the class

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Another phone constructor")

        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def show(self):
        print(self.__price)

class SmartPhone(Phone):
    def check(self):
        print(self.__price)

s = SmartPhone(2000,"apple",13)
print(s.brand) # here brand is not private so it can access atrribute
s.check() # here price is private attribute it can't access