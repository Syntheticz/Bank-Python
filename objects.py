from enum import Enum
from csv import DictWriter, DictReader
from io import StringIO


class TransactionType(Enum):
    WITHDRAW = "WITHDRAW"
    DEPOSIT = "DEPOSIT"
    TRANSFER = "TRANSFER"
    BALANCE_INQUIRY = "BALANCE INQUIRY"
    GENERATE_RECEIPT = "GENERATE RECEIPT"

class ErrorType(Enum):
    ACCOUNT = "ACCOUNT"
    TRANSACTION = "TRANSACTION"
    VALIDATION = "VALIDATION"
    AUTHENTICATION = "AUTHENTICATION"


class Account:
    PIN_LENGTH = 4

    def __init__(self, account_number=None, name=None, date_of_birth=None, PIN=None, encrypted_account_bal=None,
                 account_balance=0.0, isActive=True):
        self.account_number = account_number
        self.name = name
        self.date_of_birth = date_of_birth
        self.PIN = PIN
        self.encrypted_account_bal = encrypted_account_bal
        self.account_balance = account_balance
        self.isActive = isActive

    def __str__(self):
        return f"Account(name={self.name}, account_number={self.account_number}, date_of_birth={self.date_of_birth}, PIN={self.PIN}, encrypted_account_bal={self.encrypted_account_bal}, account_balance={self.account_balance}, isActive={'Yes' if self.isActive else 'No'})"

    def to_csv(self):
        fieldnames = [
            "account_number",
            "name",
            "date_of_birth",
            "PIN",
            "encrypted_account_bal",
            "account_balance",
            "isActive"
        ]

        with StringIO() as csv_string:
            writer = DictWriter(csv_string, fieldnames=fieldnames)
            writer.writerow(vars(self))
            csv_string.seek(0)
            return csv_string.read().strip()
    
    @classmethod
    def from_csv(self, csv_string):
        fieldnames = [
            "account_number",
            "name",
            "date_of_birth",
            "PIN",
            "encrypted_account_bal",
            "account_balance",
            "isActive"
        ]

        reader = DictReader(StringIO(csv_string), fieldnames=fieldnames)
        account_data = next(reader)
        
        return self(
            account_data["account_number"],
            account_data["name"],
            account_data["date_of_birth"],
            account_data["PIN"],
            account_data["encrypted_account_bal"],
            account_data["account_balance"],
            account_data["isActive"]
        )


class TransactionLog:
    def __init__(self):
        self.transactionType = TransactionType
        self.transactionID = "" # Must be unique
        self.timeStamp = ""
        self.issuedAmount = 0.0
        self.accountNumber = ""
        self.remarks = ""

class ErrorHandling :
    def __init__(self):
        self.errorType = ErrorType
        self.errorMessahe = ""
        self.timeStamp = ""
        self.accountNumber = ""
