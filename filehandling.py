from os import path, makedirs
from objects import Account as ACCOUNT
from random import randint

import importlib
import sys


import subprocess
import time


FILENAME = "Records.txt"
FILEPATH = ["ATM", "ADMIN"]
CARD_PATH= ""
KEY =5

def saveAccount(account):
    temp = account
    encrypt_account(temp, KEY)
    
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
    
def save_to_card(account_number : str):
    account = retrieve_by_account_number(CARD_PATH, account_number)
    if account is None:
        print("Error")
        return
    

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

def check_removable_drive():
    # Run system command to get drive information
    cmd = "wmic logicaldisk get caption, drivetype"
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")

    # Parse the output to extract removable drives
    drives = []
    lines = output.strip().split("\n")[1:]
    for line in lines:
        drive, drivetype = line.split()
        if int(drivetype) == 2:
            drives.append(drive)

    return drives

def get_removable_drive_path(drive_letter):
    cmd = "wmic logicaldisk where caption='{}' get name".format(drive_letter)
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    lines = output.strip().split("\n")
    if len(lines) >= 2:
        drive_path = lines[1].strip()
        return drive_path
    return None

import time
import subprocess
from os import path

def initial_card_check():
    # Initial check for removable drives
    global CARD_PATH

    previous_drives = check_removable_drive()
    print("Please insert Flash Drive...")

    # Wait for a short interval before checking again
    interval = 0.5  # in seconds
    time.sleep(interval)

    # Check for removable drives
    current_drives = check_removable_drive()

    # Compare current and previous drives to detect changes
    added_drives = [drive for drive in current_drives if drive not in previous_drives]
    removed_drives = [drive for drive in previous_drives if drive not in current_drives]

    # Handle added and removed drives
    if added_drives:
        print("Card Inserted")
        print("Validating...")
        drive_path = get_removable_drive_path(added_drives[0])
        file_path = f"{drive_path}\\record.txt"
        print(file_path)
        if not path.isfile(file_path):
            return False
        else:   
            return True

    if removed_drives:
        print("Please Insert Your Card!")
        return None
        

    # Update the previous drives list
    previous_drives = current_drives

def read_card(file_path):
    global KEY
    with open(file_path, 'r') as file:
        data = file.readline().strip()
        KEY = int(file.readline().strip())
        account = ACCOUNT.from_csv(data)
        retrieved_account : ACCOUNT = retrieve_by_account_number(f"{FILEPATH[0]}\\{FILENAME}", account.account_number)
        if retrieved_account is None:
            return None
        return retrieved_account
        
def is_card_inserted(file_path):
    if not path.isfile(file_path):
        return False
    else:
        return True

def save_to_card():
    if not is_card_inserted():
        return
    
def test_run(account : ACCOUNT):
    if not is_card_inserted or account is None:
        print("There was an error")
        return
    
    decrypt_account(account, KEY)
    print("WELCOME, " + account.name)


