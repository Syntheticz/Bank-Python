import random
from objects import Account
from datetime import datetime




""""
    TO-DO:
	ATM CHECKER
        ENCRYPTION
        SAVING
        LOGGING
        CHECKSUM
 """




#REGISTRATION

def register(account):
    account.name = get_name()
    account.date_of_birth = get_bday()
    account.PIN= get_PIN()
    account.account_number = generate_account_number(existing_account_numbers)
    account.account_balance= get_initial_deposit()

    """"
    TO-DO:
        ENCRYPTION
        SAVING
        LOGGING
        CHECKSUM

    """
    print("Registration successful!")
    print("Name:", account.name)
    print("Date of Birth:", account.date_of_birth)
    print("PIN:", account.PIN)
    print("Account Number: ", account.account_number)
    print("Account Balance:", account.account_balance)

def get_name():
    while True:
        name = input("Enter Your Name: ")
        if validate_name(name):
            return name.title()
        else:
            print("Invalid name. Please enter only letters and spaces.")
            

def get_bday():
    while True:
        bdate = input("Enter Your Birthday (YYYY-MM-DD): ")
        if validate_date_of_birth(bdate):
            return bdate
        else:
            print("Invalid input. Enter a valid date of birth.")
            

def get_PIN():
    while True:
        pin=input("Enter your pin: ")
        if validate_PIN(pin):
            while True:
                confirm_pin = input("Confirm your pin: ")
                if validate_PIN(confirm_pin):
                    if verify_PIN(pin,confirm_pin):
                        return pin
                    else:
                        print("PIN not matched. Try again.")
                else:
                    print("Invalid input. Enter a valid PIN.")        
        else:
            print("You have entered an invalid PIN. Try Again.")
            

def verify_PIN(pin, confirm_pin):
    return pin == confirm_pin       
     
def generate_account_number(existing_account_numbers):
    while True:
        account_number = random.randint(100000, 999999)
        if account_number not in existing_account_numbers:
            return account_number
        else:
            generate_account_number()
        
def get_initial_deposit():
    while True:
        user_balance= input("Initial Deposit [Minimum of 10000.00]:")
        if validate_initial_deposit(user_balance):
            return user_balance
        else:
            print("Enter a valid amount!")
            


def compare_account_bal(amount,user_balance):
    if user_balance > amount:
        return True
    return False





#LOGIN

def login(client):
    while True:
        pin = input("Enter your PIN: ")
        if verify_PIN(client.PIN, pin):
            print("Login successful!")  # Print a message to indicate successful login
            print(client.PIN)  # Print the client details

            # Rest of the function logic
            
        else:
            print("You have entered a wrong PIN!")
            






#TRANSACTION



def deposit(client):
    while True:
        amount = input("Enter amount to deposit: [min 100.00]")
        amount = float(amount)
        if validate_amount(amount):
            client.account_balance += amount
            print(client.account_balance)
            break
            #save the updated balance
            #log the transaction
            #checksum
        else:
            print("Invalid Amount.")

    """"
    TO-DO:
        ENCRYPTION
        SAVING
        LOGGING
        CHECKSUM

    """
            

def withdraw(client):
    while True:
        amount= input ("Enter amount to withdraw: [min 100.00]")
        amount= float(amount)

        if validate_amount(amount) and compare_account_bal(amount,client.account_balance):
            client.account_balance -= amount
            #save the updated balance
            #log the transaction
            #checksum
        else:
            print("Invalid Amount.")

    """"
    TO-DO:
        ENCRYPTION
        SAVING
        LOGGING
        CHECKSUM

    """
            
def transfer(client, recipient):
    while True:
        amount = input("Enter amount to transfer: ")
        amount = float(amount)
        if validate_amount(amount) and compare_account_bal(amount,client.account_balance):
            client.account_balance -= amount
            recipient.account_balance += amount
            print(client.account_balance, recipient.account_balance)
        else:
            print ("Invalid Amount.")
        

#VALIDATION
def validate_name(name):
    if name.replace(" ", "").isalpha():
        return True
    return False

def validate_date_of_birth(date_of_birth):
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        current_date = datetime.now().date()
        if dob.year > 1900 and dob.date() <= current_date:
            return True
        return False
    except ValueError:
        return False

def validate_PIN(pin):
    if pin.isdigit() and len(pin) == 4:
        return True
    return False;

def validate_initial_deposit(amount):    
    if float(amount) >= 10000.00:
        return True
    return False


def validate_amount(amount):
    if amount >=100:
        return True
    return False


def account_summary(client):
    #retrieve first from file the latest account summary of the current client
    print("Your balance is: " + client.account_balance)    





#simulating existing account numbers from database
#for actual implementation, you can either retrieve all accnumbers from the file and pass it in this list, or just check the file one by one.
existing_account_numbers = ["000000", "111111", "6666666", "654321"]  # List of existing account numbers

client = Account()
recipient = Account()

"""
client.name= "Alexander Rosete"
client.account_number= "123456"
client.encrypted_account_bal = ""
client.account_balance= 15000.00
client.PIN = "0000"
client.isActive = True

login(client)


register(client)
"""
"""
#Transfer Tester (recipient)

recipient = Account()
recipient.name = "Phil Guiang"
recipient.account_number = "654321"
recipient.encrypted_account_bal= ""
recipient.account_balance = 5000.00
recipient.PIN= "1234"
recipient.isActive = True

login(client)

"""
""" #Registration Tester:

new_account = Account()

# Call the register function
register(new_account)


"""
