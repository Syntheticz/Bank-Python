from enum import Enum


# Liblaries
import datetime
import uuid
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

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
    def __init__ (self):
        self.transactionType = TransactionType
        self.timeStamp = ""
        self.issuedAmount = 0.0
        self.accountNumber = ""
        self.remarks = ""
    
    def transactionLog (self) :
        return f"[{self.time_stamp}] Transaction Type: {self.transaction_type} | Account Number: {self.account_number} | Amount: P{self.issued_amount} | Status: {self.remarks}"

    def userLoginLog (self) :
        self.login_time = datetime.datetime.now()
        return f"User '{self.account_number}' logged in at [{self.curr_time}]."
    
    def userLogoutLog (self) :
        self.logout_time = datetime.datetime.now()
        return f"User '{self.account_number}' logged out at [{self.curr_time}]."

    # Error Logs

    def invalidUsernameLog (self) :
        self.curr_time = datetime.datetime.now()
        return f"Invalid Username at [{self.curr_time}]."

    def invalidPasswordLog (self) :
        self.curr_time = datetime.datetime.now()
        return f"Invalid Password at [{self.curr_time}]."

    def wrongPasswordLog (self) :
        self.curr_time = datetime.datetime.now()
        return f"Incorrect password for Account number: {self.account_number} at [{self.curr_time}]."

    def invalidAmountLog (self) :
        self.curr_time = datetime.datetime.now()
        return f"Account Number: {self.account_number} attempts to {self.transaction_type} an invalid amount at [{self.curr_time}]."

class DocumentGenerator:

    def __init__(self):
        self.filename = "r.pdf"
        self.page_width, self.page_height = letter
        self.canva = canvas.Canvas(self.filename, pagesize=letter)
        self.canva.setFont("Helvetica", 12)
        self.canva.setLineWidth(1);

        # Generate a random reference number
        self.reference_number = str(uuid.uuid4())

        # Get DateTime
        dt = datetime.datetime.now()
        self.curr_dt = dt.isoformat()

        self.account_number = ""
        self.transaction_type = TransactionType
        self.amount = ""

        
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
        self.canva.line(100, 300, 512, 200)

        self.canva.drawString(self.centerXPos("Thank you for using OUR BANK ATM!"),270, "Thank you for using OUR BANK ATM!")
        
        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 250, 512, 100)

        # Save the document
        self.canva.save()

        print("Saved")

    def generateReport(self) :
        
        self.frequency_usage = 0;
        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 700, 512, 700)

        self.canva.drawString(self.centerXPos("Monthly Report"), 660, "Monthly Report")

        self.canva.drawString(self.centerXPos("OUR BANK"),630, "OUR BANK")

        self.canva.setDash([4, 2])  # Set the dash pattern (4 units on, 2 units off)
        self.canva.line(100, 600, 512, 600)

        self.canva.drawString(100,550, "Account Number:  " + str(self.account_number))
        self.canva.drawString(130,530, "Frequency Usage :  " + str(self.frequency_usage))
        self.canva.drawString(130,510, "Transactions:  ")

        # Define table data
        data = [
            ["Transaction Type", "Amount", "Date|Time"],
            ["Deposit", "100", "time"],
            ["Withdraw", "100", "date"],
            ["Transfer", "100", "datetim"],
        ]

        # populate data 
        # Iterate over the dictionary and populate the table data
        # for key, values in transaction_data.items():
        #     transaction_type = values["TransactionType"]
        #     amount = values["Amount"]
        #     datetime = values["DateTime"]

        #     # Add a row to the data list
        #     data.append([transaction_type, amount, datetime])


        # Set table style
        table_style = [
            ("BACKGROUND", (0, 0), (-1, 0), colors.white),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.white),          
        ]

        # Create table object
        table = Table(data,100,20)

        # Apply table style
        table.setStyle(table_style)

        # Apply table style
        table.setStyle(table_style)

        # Calculate table width and height
        table_width, table_height = table.wrapOn(self.canva, 400, 200)

        # Position the table on the canvas
        table_x = (letter[0] - table_width) / 2
        table_y = (letter[1] - table_height) / 2
        table.drawOn(self.canva, table_x , table_y + 50)
        # Save the document 
        self.canva.save()

        print("saved")

class ErrorHandling :
    def __init__(self):
        self.errorType = ErrorType
