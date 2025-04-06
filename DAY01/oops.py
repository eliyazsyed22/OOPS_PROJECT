# Understand oops concept

# class is written in pascalcase #AtmMachine

""" classes are two types
    built in class
    userdefined class """
class Atm:
    
    
    # constructor
    """ If you specify a method in constructor it will call method automatically when the object is defined """
    def __init__(self):
        
        # attributes (variables when defined outside constructor)
        self.pin = ""
        self.balance = 0
        self.menu()
        
        
    def menu(self):
        user_input = input(""" 
                            Hi How Can I help You

                            1. Press 1 to create a Pin
                            2. Press 2 to change Pin
                            3. Press 3 to check balance
                            4. Press 4 to withdraw balance
                            5. Press 5 to exit 
                            \n                    """)
        
    
        if user_input == "1":
            self.create_pin()        
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.with_draw()
        else:
            exit()
        
        
    def create_pin(self):
        user_pin = input("Enter your pin \n")
        self.pin = user_pin
        
        user_balance = int(input("Enter your balance \n"))
        self.balance = user_balance
        
        print("Pin created Successfully")
        self.menu()
        
    def change_pin(self):
        old_pin = input("Enter your old pin")
        
        if old_pin == self.pin:
            
            new_pin = input("please type your new pin \n")
            self.pin = new_pin
            print("Pin changed successfully")
            self.menu()
        else:
            print("You're old pin not matches please try again")
            self.menu()
            
    
    
    def check_balance(self):
        user_pin = input("Enter your pin \n")

        if user_pin == self.pin:
            print(f"your balance is {self.balance}")
        else:
            print("You have entered wrong pin")
            self.menu()
            
            
    def with_draw(self):
        user_pin = input("Enter your pin \n")
        
        if user_pin == self.pin:
            user_amount = int(input("Enter the amount \n"))

            if user_amount <= self.balance:
                self.balance = self.balance - user_amount
                print(f"with draw success, remaining balance is {self.balance}")
            elif user_amount > self.balance:
                print("Insufficient funds")     
        else:
            print("wrong pin attempted")
            
        # here calling menu out of loop 
        self.menu()





        
        

        
        
        

obj = Atm()



        
        
        