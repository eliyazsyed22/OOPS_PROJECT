# a = 3/4 * 1/2
# print(a)

# python doesn't have data type fraction we are creating our own data type fraction

class Fraction:
    
    
    # parameterized constructor "It requires some inputs"
    def __init__(self,x,y):
        self.num = x
        self.den = y
        
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        new_num = self.num * other.den + other.num * self.den 
        new_den = self.den * other.den 
        
        return "{}/{}".format(new_num,new_den)
    
    
    def __sub__(self,other):
        new_num = self.num * other.den - other.num * self.den 
        new_den = self.den * other.den 
        
        return "{}/{}".format(new_num,new_den)
    
    
    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den 
        
        return "{}/{}".format(new_num,new_den)
    
    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num 
        
        return "{}/{}".format(new_num,new_den)
    

        
        
        
        
    


Fr1 = Fraction(2,4)
Fr2 = Fraction(3,4)

print(Fr1+Fr2)
print(Fr1-Fr2)
print(Fr1*Fr2)
print(Fr1/Fr2)
