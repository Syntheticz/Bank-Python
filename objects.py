from enum import Enum


# Liblaries
import datetime
import uuid
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from csv import DictWriter, DictReader
from io import StringIO

from reportlab.platypus import Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph

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

    def __copy__(self):
        obj = Account(self.account_number, self.name, self.date_of_birth, self.PIN, self.encrypted_account_bal,
                            self.account_balance, self.isActive)
        return obj
    
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
    def __init__ (self):
        self.transactionType = TransactionType
        self.timeStamp = ""
        self.issuedAmount = 0.0
        self.accountNumber = ""
        self.remarks = ""
    
    def transactionLog (self) :
        return f"[{self.timeStamp}] | Transaction Type: {self.transactionType} | Account Number: {self.accountNumber} | Amount: P{self.issuedAmount} | Status: {self.remarks}"

    def userLoginLog (self) :
        self.login_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        return f"User '{self.accountNumber}' logged in at [{self.login_time}]."
    
    def userLogoutLog (self) :
        self.logout_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        return f"User '{self.accountNumber}' logged out at [{self.logout_time}]."

    # Error Logs

    def invalidUsernameLog (self) :
        self.curr_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        return f"Invalid Username at [{self.curr_time}]."

    def invalidPasswordLog (self) :
        self.curr_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        return f"Invalid Password at [{self.curr_time}]."

    def wrongPasswordLog (self) :
        self.curr_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        return f"Incorrect password for Account number: {self.accountNumber} at [{self.curr_time}]."

    def invalidAmountLog (self) :
        self.curr_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")    
        return f"Account Number: {self.accountNumber} attempts to {self.transactionType} an invalid amount at [{self.curr_time}]."


class DocumentGenerator:

    def __init__(self, doc_path):
        self.page_width, self.page_height = letter
        self.canva = canvas.Canvas(doc_path, pagesize=letter)
        self.canva.setFont("Helvetica", 12)
        self.canva.setLineWidth(1)

        self.doc = SimpleDocTemplate(doc_path, pagesize=letter)
        self.elements = []
        self.styles = getSampleStyleSheet()
        # Generate a random reference number
        self.reference_number = str(uuid.uuid4())

        # Get DateTime
        dt = datetime.datetime.now()
        self.curr_dt = dt.isoformat()

        self.account_number = ""
        self.transaction_type = TransactionType
        self.amount = ""

        self.table_y = self.page_height - 50

        
    def centerXPos(self, text):
        text_width = self.canva.stringWidth(text, "Helvetica", 12)
        x = (self.page_width - text_width) / 2
        return x
    

    def generateReceipt(self) :

        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 700, 512, 700)

        self.canva.drawString(self.centerXPos("TRANSACTION RECEIPT"), 660, "TRANSACTION RECEIPT")

        self.canva.drawString(self.centerXPos("OUR BANK"),630, "OUR BANK")

        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 600, 512, 600)

        self.canva.drawString(100,550, "Date/Time:              " + str(self.curr_dt))
        self.canva.drawString(100,500, "Account Number :        " + str(self.account_number))
        self.canva.drawString(100,450, "Transaction Type:       " + str(self.transaction_type))
        self.canva.drawString(100,400, "Amount:                 " + str(self.amount))

        self.canva.drawString(100,350, "Reference ID:           " + str(self.reference_number))
       
        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 300, 512, 300)

        self.canva.drawString(self.centerXPos("Thank you for using OUR BANK ATM!"),270, "Thank you for using OUR BANK ATM!")
        
        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 250, 512, 250)

        # Save the document
        self.canva.save()

        print("Saved")


    def generateReport(self) :

        self.frequency_usage = 0;
        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 700, 512, 700)

        self.canva.drawString(self.centerXPos("Monthly Report"), 660, "Monthly Report")

        # Set styles for the headings
        heading1_style = ParagraphStyle(
            name="Heading1",
            parent=self.styles["Heading1"],
            alignment=1,
            spaceAfter=0.5 * inch
        )
        heading2_style = ParagraphStyle(
            name="Heading2",
            parent=self.styles["Heading2"],
            alignment=1,
            spaceAfter=0.25 * inch
        )

        # Prepare the table data
        data = [  
        ]

        self.elements.append(Paragraph("<b>Monthly Report</b>", heading1_style))
        self.elements.append(Paragraph("<b>OUR BANK</b>", heading2_style))
        self.elements.append(Spacer(1, 0.5 * inch))
        
        from filehandling import read_log_files

        account_details = read_log_files()

        # Iterate over the records and populate the table data
        for account_number, details in account_details.items():
            frequency_usage = details["FrequencyUsage"]
            transactions = details["Transactions"]

            # Add frequency usage to the table
            data.append(["Account Number: " + str(account_number)])
            data.append(["Frequency Usage: " + str(frequency_usage)])
            data.append(["Transaction Type", "Amount", "Date|Time"]);
            data.append([])  # Add an empty row
            
            # Add transaction details to the table
            for transaction in transactions:
                transaction_type = transaction["TransactionType"]
                amount = transaction["Amount"]
                datetime = transaction["DateTime"]
                data.append([transaction_type, str(amount), datetime])

            data.append([])  # Add an empty row after each account

        # Set table style
        table_style = [
            ("BACKGROUND", (0, 0), (-1, 0), colors.white),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("WORDWRAP", (0, 0), (-1, -1), True),
        ]
        
        # Create table object
        table = Table(data, colWidths=[100, 100, 150])

        table.setStyle(table_style)

        self.elements.append(table)

        self.doc.build(self.elements)

        print("Saved")


    def calculateTableHeight(self, table):
        table.wrapOn(self.canva, 400, 200)
        return table._height

        print("saved")

class ErrorHandling :
    def __init__(self):
        self.errorType = ErrorType
        self.errorMessahe = ""
        self.timeStamp = ""
        self.accountNumber = ""
