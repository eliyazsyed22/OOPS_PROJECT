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


# s = SmartPhone(2000,'Apple',13)

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
       
       
       
    # here it acts like a getter method 
    def show(self):
        print(self.__price)

class SmartPhone(Phone):
    def check(self):
        print(self.__price)

""" s = SmartPhone(2000,"apple",13)
print(s.brand) # here brand is not private so it can access atrribute
s.show() # here price is a private variable how ever it access

# s.check() # here price is private attribute it can't access """





# Example - 1

class Parent:
    
    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):
    
    def show(self):
        print("This is in child class")


son = Child(100)

# print(son.get_num())
# son.show()
        
        
        
# Example - 2


class Parent:
    
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    
    def __init__(self,val, num):
        self.__val = val
        
    def get_val(self):
        return self.__val
    
son = Child(100,10)



# in this example child has own constructor so it will not call to parent class we are asking to get_num value to it will not intiliaze and through attribute error
# print("parent: Num: ",son.get_num())
# print("child: Num:",son.get_val())



# example 3

class A:
    
    def __init__(self):
        self.var1 = 1000

    def display1(self,var1):
        print("class A:", self.var1)


class B(A):
    
    def display2(self,var1):
        print("class B:",self.var1)

obj = B()


# here self.var1 and passed var1 both are different variables
# obj.display1(200)


# Method over-riding

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    
    # here already in parent class buy defined we over rided again in child class
    def buy(self):
        print("Buying a smartphone")

s = SmartPhone(2000,"apple",13)

s.buy()
        
        




    