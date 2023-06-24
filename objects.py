from enum import Enum

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

    def __init__(self):
        self.name = ""
        self.account_number = ""
        self.date_of_birth = ""
        self.PIN = ""
        self.encrypted_account_bal = ""
        self.account_balance = 0.0
        self.isActive = True

    def __str__(self):
        return f"Account(name={self.name}, account_number={self.account_number}, date_of_birth={self.date_of_birth}, PIN={self.PIN}, encrypted_account_bal={self.encrypted_account_bal}, account_balance={self.account_balance}, isActive={'Yes' if self.isActive else 'No'})"


class TransactionLog:
    def __init__(self):
        self.transactionType = TransactionType
        self.timeStamp = ""
        self.issuedAmount = 0.0
        self.accountNumber = ""
        self.remarks = ""

class ErrorHandling :
    def __init__(self):
        self.errorType = ErrorType
