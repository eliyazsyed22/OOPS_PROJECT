# Example

class Customer:
    
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
        
        
    def print_adress(self):
        print(self.address.city,self.address.pincode,self.address.state)
          
class Address:
    
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
    

add1 = Address('hyd',500009,'ts')  
cust = Customer('rana','male',add1)


cust.print_adress()
