# need for static varibales
#If you want a counter for varibale increase by 1 every time instance varibale will be not be work so you can use static varibale

class Atm:
    
    # static varibale
    __counter = 1
    
    def __init__(self):
        self.pin = ""
        #here when use instance varibale will call with object(self is object)
        self.balance = 0
        
        # here when use static varibale will call with class
        self.cid = Atm.counter
        Atm.counter = Atm.counter + 1
        
    
    # static method or utility functions
    # these methods are not related to object they related to class
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    
    
# access getter method with out self

c1 = Atm.get_counter()
        