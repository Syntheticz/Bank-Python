from os import path, makedirs
from objects import Account as ACCOUNT

FILENAME = "Records.txt"
FILEPATH = ["ATM", "ADMIN"]
KEY =5

def saveAccount(account):
    encrypt_account(account, KEY)
    
    for PATH in FILEPATH:
        if not path.exists(PATH):
            makedirs(PATH)
        if not path.isfile(f"{PATH}/{FILENAME}"):
             with open(f"{PATH}/{FILENAME}", "w") as file:
                pass
        save(f"{PATH}/{FILENAME}", account)
    

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

