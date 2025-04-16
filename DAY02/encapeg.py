#example for encapsulation

class Person:
    
    def __init__(self):
        self.__name = "nitish"
        


p1 = Person()
p1.__name = "ankit"

print(p1.__name)