# list of objects

class Person:
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        
p1 = Person("nitish","male")
p2 = Person("ankit","male")
p3 = Person("ankita","female")

# l = [p1,p2,p3]


# for i in l:
#     print(i.name,i.gender)
    
    
# dictionary of objects

class Person:
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


p1 = Person("rahul","male")
p2 = Person("dhoni","male")
p3 = Person("juhulan","female")

d = {
    "p1" : p1,
    "p2" : p2,
    "p3" : p3
}

for i in d:
    print(d[i].name,d[i].gender)