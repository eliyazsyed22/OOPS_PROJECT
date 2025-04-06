# This method is also called as dunder method

# constructor - It is a special method which doesn't require to call it will be called when object is created

class Temp:
    
    def __init__(self):
        print("hello")
        
# true benefit of constructor
# to write configuration related code
# basically under constructor you can write code which doesn't depend on user like code to connect with database or connect to internet

obj = Temp()