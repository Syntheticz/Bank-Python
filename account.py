import random
from objects import Account
import filehandling
from filehandling import fetch_acc, save_account, save_account_current,  decrypt_account, fetch_card_contents, retrieve_key
from datetime import datetime

#TESTER:
client = Account()
current_user = Account()
recipient = Account()


temp_account_finder = fetch_card_contents()

current_key = temp_account_finder[1]
decrypt_accnum = decrypt_account(temp_account_finder[0], temp_account_finder[1])
current_user = decrypt_accnum









""""
    TO-DO:
        RETRIEVE: use fetch_acc(accnum, KEY)
        SAVING: user saveAccount(class account)
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
    if user_balance >= amount:
        return True
    return False





#LOGIN

def login(pin):
  
    
    #RETRIEVE HERE - CLIENT DETAILS using retrieved accountnumber from records.txt, specially client.PIN, function name: fetch_acc()
    
    enc_client = fetch_acc (current_user.account_number, current_key)
    client = decrypt_account(enc_client, current_key)
    
    #compare pin:
    while True:
        if verify_PIN(client.PIN, pin):
            print("Login successful!")  # Print a message to indicate successful login
            print(client.PIN)  # Print the client details
            filehandling.saveUserLogin(client.account_number)
            return True
            break
            # Rest of the function logic
            
        else:
            print("You have entered a wrong PIN!")
            filehandling.saveWrongPasswordLog(client.account_number)
            return False
            break
            






#TRANSACTION



def deposit(amount):
    #RETRIEVE HERE - retrieve client details, most importantly client.account_balance
    enc_client = fetch_acc (current_user.account_number, current_key)
    client = decrypt_account(enc_client, current_key)
    while True:
        amount = float(amount)
        if validate_amount(amount):
            client.account_balance += amount
            print(client.account_balance)
            #SAVE HERE - update balance of user
            save_account_current(client)
            #LOG HERE - account number: client.account_number, trasaction: deposit, amount: amount
            filehandling.saveTransactionLog("Deposit",amount,client.account_number,"Success")
            break
            
        else:
            filehandling.saveInvalidAmountLog(client.account_number, "Deposit")
            print("Invalid Amount.")

    """"
    TO-DO:
        ENCRYPTION
        SAVING
        LOGGING
        CHECKSUM

    """
            

def get_userBal():
    enc_client = fetch_acc (current_user.account_number, current_key)
    client = decrypt_account(enc_client, current_key)
    return round(client.account_balance,2)

def withdraw(amount):
    #RETRIEVE HERE - retrieve client details, most importantly client.account_balance

    enc_client = fetch_acc (current_user.account_number, current_key)
    client = decrypt_account(enc_client, current_key)
    while True:
        
        amount= float(amount)

        if validate_amount(amount) and compare_account_bal(amount,client.account_balance):
            client.account_balance -= amount
            print(client.account_balance)
            #SAVE HERE - update balance of user
            save_account_current(client)

            #LOG HERE - account number: client.account_number, trasaction: deposit, amount: amount
            filehandling.saveTransactionLog("Withdraw",amount,client.account_number,"Success")
            break
 
        else:
            print("Invalid Amount.")
            filehandling.saveInvalidAmountLog(client.account_number, "Withdraw")
            break

    """"
    TO-DO:
        ENCRYPTION
        SAVING
        LOGGING
        CHECKSUM

    """
         
def receiver(account_receiver):
    global recipient
    # RETRIEVE KEY ENCRYPTION OF RECIPIENT ACCOUNT
    key = retrieve_key(account_receiver)
    print(key)
    if key is None:
        return False
    else:
        # RETRIEVE HERE RECEIVER ACCOUNT USING the account number from account_receiver
        current_recipient = fetch_acc(account_receiver, int(key[1]))
        recipient = decrypt_account(current_recipient, int(key[1]))
        
        return True


def transfer(amount,recipient_account_number):
    
    # RETRIEVE HERE - retrieve client/sender details, most importantly client.account_balance
    # sender:
    enc_client = fetch_acc(current_user.account_number, current_key)
    client = decrypt_account(enc_client, current_key)

    # recipient:
    key = retrieve_key(recipient_account_number)
    current_recipient = fetch_acc(recipient_account_number, int(key[1]))
    recipient = decrypt_account(current_recipient, int(key[1]))
    print (recipient)
    while True:
        amount = float(amount)
        if validate_amount(amount) and compare_account_bal(amount, client.account_balance):
            client.account_balance -= amount
            recipient.account_balance += amount
            print("SENDER:", client.account_balance, "RECIPIENT:", recipient.account_balance)
            # SAVE HERE- updated balance of client and update balance of recipient
            #save client:
            save_account_current(client)
            #log:
            filehandling.saveTransactionLog("Transfer",amount,client.account_number,"Success")
            #save_recipient:
            save_account(recipient,int(key[1]))
            filehandling.saveTransactionLog("Received",amount,recipient.account_number,"Success")
            # CHECKSUM HERE-
            break
        else:
            filehandling.saveInvalidAmountLog(client.account_number, "Transfer")
            print("Invalid Amount.")
            break

def account_summary():
    #RETRIEVE HERE - Account details of user
    #client = retrieved details NOTE: client here is a class
    
    enc_client = fetch_acc (current_user.account_number, current_key)
    #Decrypt encrypted client
    client = decrypt_account(enc_client, current_key)
    
    print("Your balance is: ", client.account_balance)
    
    return client 

def balance_inquiry():
    #RETRIEVE HERE - Account details of user
    #client = retrieved details NOTE: client here is a class
    
    enc_client = fetch_acc (current_user.account_number, current_key)
    #Decrypt encrypted client
    client = decrypt_account(enc_client, current_key)
    
    print("Your balance is: ", client.account_balance)
    filehandling.saveTransactionLog("Balance Inquiry",0.00,client.account_number,"Success")
    return client     

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
    return False

def validate_initial_deposit(amount):    
    if float(amount) >= 10000.00:
        return True
    return False


def validate_amount(amount):
    if amount >=100:
        return True
    return False


 





#simulating existing account numbers from database
#for actual implementation, you can either retrieve all accnumbers from the file and pass it in this list, or just check the file one by one.
existing_account_numbers = ["000000", "111111", "6666666", "654321"]  # List of existing account numbers



"""
client.name= "Alexander Rosete"
client.account_number= "123456"
client.encrypted_account_bal = ""
client.account_balance= 15000.00
client.PIN = "0000"
client.isActive = True

login(client)

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
