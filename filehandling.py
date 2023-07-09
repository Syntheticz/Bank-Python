import os
import psutil
from os import path, makedirs
from objects import Account as ACCOUNT
from random import randint
from copy import copy

import importlib
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



import subprocess
import time


FILENAME = "Records.txt"
FILEPATH = ["ATM", "ADMIN"]
CARD_PATH= ""

KEY = 5



def saveAccount(account : ACCOUNT):
    temp = copy(account)
    card_path = f"{get_card_path()}\\record.txt"
    

    #check if the card is inserted
    if not is_card_inserted(card_path):
        print("Card is not inserted")
        return

    #Checks if record exist
    card_acc = get_account_from_card(card_path)
    if card_acc is None:
        print("Records does not match any of our records must be because the record is tampered or has the wrong card")
        return

    #Can be 16 but 10 is safer 
    key = randint(1, 5)
    encrypt_account(temp, key)
    

    for PATH in FILEPATH:
        if not is_card_inserted:
            print("Error!")
            return
        if not path.exists(PATH):
            makedirs(PATH)
        if not path.isfile(f"{PATH}/{FILENAME}"):
             with open(f"{PATH}/{FILENAME}", "w") as file:
                pass
        save(f"{PATH}/{FILENAME}", temp)
    save_to_card(temp, card_path, key)

    

def save_to_card(account : ACCOUNT, card_path : str, key : int):
    if account is None:
        print("Error")
        return
    with open(card_path, "w") as file:
        file.write(f"{account.to_csv()} \n")
        file.write(str(key))

def save(filepath: str, account: ACCOUNT):
    if not path.isfile(filepath):
        with open(filepath, "w") as file:
            pass

    existing_account = retrieve_by_account_number(filepath, account.account_number)
    if existing_account is not None:
        # Overwrite the specific record
        overwrite_record(filepath, existing_account, account)
    else:
        # Append the new account to the end of the file
        with open(filepath, "a") as file:
            acc_str = f"{account.to_csv()}\n"
            file.write(acc_str)

def retrieve_by_account_number(filepath: str, account_number: str):
    if not path.isfile(filepath):
        return None

    with open(filepath, "r") as file:
        for line in file:
            csv_string = line.strip()
            account = ACCOUNT.from_csv(csv_string)
            if account.account_number == account_number:
                return account
        return None
    

def overwrite_record(filepath: str, existing_account: ACCOUNT, new_account: ACCOUNT):
    lines = []
    updated = False

    with open(filepath, "r") as file:
        for line in file:
            csv_string = line.strip()
            account = ACCOUNT.from_csv(csv_string)
            if account.account_number == existing_account.account_number:
                acc_str = new_account.to_csv()
                lines.append(acc_str)
                updated = True
            else:
                lines.append(csv_string)

    lines[len(lines) - 1] += "\n"

    if updated:
        with open(filepath, "w") as file:
            write_str = "\n".join(lines)
            file.write(write_str)


def swap_chars(string, key):
    return ''.join(chr(ord(char) + key) for char in string)

def restore_chars(string, key):
    return ''.join(chr(ord(char) - key) for char in string)


def encrypt_decimal(amount, key):
    converted_amount = swap_chars(str(int(round(amount * 100))), key)
    return converted_amount

def decrypt_decimal(amount : str, key):
    converted_amount = int(restore_chars(amount, key))
    return converted_amount / 100.0

def encrypt_account(account, key):
    account.name = ''.join(chr(ord(char) + key) for char in account.name)
    account.account_number = ''.join(chr(ord(char) + key) for char in account.account_number)
    account.date_of_birth = ''.join(chr(ord(char) + key) for char in account.date_of_birth)
    account.PIN = ''.join(chr(ord(char) + key) for char in account.PIN)
    account.encrypted_account_bal = encrypt_decimal(account.account_balance, key)
    account.account_balance = 0.0

def decrypt_account(account : ACCOUNT, key):
    account.name = ''.join(chr(ord(char) - key) for char in account.name)
    account.account_number = ''.join(chr(ord(char) - key) for char in account.account_number)
    account.PIN = ''.join(chr(ord(char) - key) for char in account.PIN)
    account.date_of_birth = ''.join(chr(ord(char) - key) for char in account.date_of_birth)
    account.account_balance = decrypt_decimal(account.encrypted_account_bal, key)
    account.encrypted_account_bal = "0"

    return account

#This is the same as get_key() but for accounts
def get_account_from_card(path):
    with open(path, 'r') as file:
        data = file.readline().strip()
        account = ACCOUNT.from_csv(data)
        if account is None:
            return None
        return account
        
def is_card_inserted(filepath : str):
    return False if not path.isfile(filepath) else True

#Fetching acc from ATM
def fetch_acc(account_number : str, key : int):
    number = swap_chars(account_number, key)
    return retrieve_by_account_number(f"{FILEPATH[0]}\\{FILENAME}", number)
    

def get_card_path():
    drives=psutil.disk_partitions()
    for drive in drives:
        if 'removable' in drive.opts and drive.mountpoint != "":
            CARD_DIRECTORY =  drive.mountpoint
            return CARD_DIRECTORY

def get_key():
    with open(f"{get_card_path()}\\record.txt", "r") as file:
        lines = file.readlines()
        key = lines[-1].strip()
    #Change the key to int
    return int(key)

#This should satisfy Card_contents
def fetch_card_contents():
    filepath = f"{get_card_path()}\\record.txt"
    if not path.isfile(filepath):
        return None
    else:
        key = get_key(filepath)
        account = get_account_from_card(filepath)
        return [account,int(key) ]
    
    # Returns: [0] the encrypted account object and  [1] the key 
    # NOTE: You'll be needing to decrypt this using the key provided or use the get_key() instead
    
accounts = [
    ACCOUNT("123456782", "Jane Smith", "1995-05-10", "5678", "encrypted1", 2000.0, True),
    ACCOUNT("987654321", "John Doe", "1990-12-15", "4321", "encrypted2", 1500.0, True),
    ACCOUNT("456789123", "Alice Johnson", "1985-08-25", "9876", "encrypted3", 3000.0, False),
    ACCOUNT("789123456", "Bob Anderson", "1998-03-05", "6543", "encrypted4", 5000.0, True),
    ACCOUNT("654321987", "Sarah Davis", "1992-07-01", "8765", "encrypted5", 1000.0, False),
    ACCOUNT("321654987", "Michael Wilson", "1980-11-20", "3456", "encrypted6", 2500.0, True),
    ACCOUNT("987123654", "Emily Thompson", "1993-09-12", "2345", "encrypted7", 4000.0, False),
    ACCOUNT("456321789", "David Brown", "1988-06-08", "7654", "encrypted8", 6000.0, True),
    ACCOUNT("789456123", "Olivia Miller", "1997-04-18", "5432", "encrypted9", 3500.0, True),
    ACCOUNT("654789321", "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz", "1991-10-30", "8765", "encrypted10", 4500.0, False)
]

while True:
    for acc in accounts:
        saveAccount(acc)
        dacc = decrypt_account(fetch_acc(acc.account_number, get_key()), get_key())
        print(dacc)