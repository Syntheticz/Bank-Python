from os import path
from objects import Account as ACCOUNT

FILENAME = "Records.txt"

def save(filepath: str, account: ACCOUNT):
    if not path.isfile(filepath):
        with open(filepath, "w") as file:
            print("File Created")

    existing_account = retrieve_by_account_number(filepath, account.account_number)
    if existing_account is not None:
        # Overwrite the specific record
        overwrite_record(filepath, existing_account, account)
    else:
        # Append the new account to the end of the file
        with open(filepath, "a") as file:
            acc_str = f"{account.to_csv()} \n"
            file.write(acc_str)

def retrieve_by_account_number(filepath: str, account_number: str):
    if not path.isfile(filepath):
        print("File does not exist")
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
                lines.append(new_account.to_csv())
                updated = True
            else:
                lines.append(csv_string)

    if updated:
        with open(filepath, "w") as file:
            file.write("\n".join(lines))

            
