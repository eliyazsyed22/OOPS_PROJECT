class Person:
    
    
    def __init__(self,name,place):
        self.name = name
        self.place = place
        self.greet()
        
    
    def greet(self):
        
        if self.place == "India":
            print(f"Hi {self.name} your are in {self.place}")
        else:
            print("You're are outsider")
        

# p = Person("eliyaz","india")

# creating attribute outside of class
# p.gender = "male"
# s = p.gender
# # print(s)


# object without a reference

""" class Person:
    
    def __init__(self):
        self.name = "nitish"
        self.gender = "male"

p = Person()
q = p

print(id(p))
print(id(q))


print(p.name)
print(q.name)

q.name = "ankit"
print(q.name)
print(p.name) """


# pass by reference

class Person:
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# outside the class hence it is a function

def greet(person):
    print("HI my name is ",person.name, "and Iam a ",person.gender )

# here we are passing an object to a function then it becomes class method

p = Person("nitish","male")
# greet(p)



# another example of pass by reference

class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        
def greet(person):
    print(id(person))
    person.name = "ankit"
    return person
    # print(person.name)
     

# imp here look even we are calling outside function here it will print ankit 
p = Person('nitish','male')
print(id(p))
p1 = greet(p)
# print(p.name)
print(id(p1))
