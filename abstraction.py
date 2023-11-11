#Abstraction in python

print("\nAbstraction\n")

class BOB :
    _balance = int(0) #bank personal balance

    def __init__(self, n, ammount):
        self.name = n
        self.balance = ammount
        BOB._balance += ammount

    def credit(self, ammount):
        self.balance += ammount
        BOB._balance += ammount
        print("Rs.",ammount, "Debited...\nYour balance is Rs.", self.balance)

    def debit(self, ammount):
        if(self.balance >= ammount):
            self.balance -= ammount
            BOB._balance -= ammount
            print("Rs.",ammount, "credited...\nYour balance is Rs.", self.balance)
        else:
            print("Insufficient balance...")

    def show(self):
        print("Your name is : ", self.name)
        print("Your balance is Rs.", self.balance)
    


print("Banking System...\n")
print("Enter details for creating account in HDFC bank...")
name = input("Enter your name : ")
ammount = int(input("Enter Ammount : "))
user = BOB(name, ammount)

while True:
    input()
    print("\n1. For Debit ammount")
    print("2. For Credit ammount")
    print("3. For See the Account details")
    print("0. For Exiting from bank")

    choice = int(input("\nWhat do you want to do : "))
    if(choice == 1):
        a = int(input("How much Rs. do you want to debit : "))
        user.debit(a)

    elif(choice == 2):
        a = int(input("How much Rs. do you want to credit : "))
        user.credit(a)
        
    elif(choice == 3):
        user.show()
        
    elif(choice == 0):
        break

    else:
        print("Invalid Choice")