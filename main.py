
from objects import DocumentGenerator

import filehandling

def run():
    print ("Hello World")
    gen = DocumentGenerator("report/report.pdf")
  
    gen.generateReport();

   

    filehandling.saveTransactionLog("Withdraw",100,"123456","Success");

 
    # Save user login log
    filehandling.saveUserLogin("12345")

  
    # Save user logout log
    filehandling.saveUserLogout("12345")

  
    # Save invalid username log
    filehandling.saveInvalidUsernameLog()

   
    filehandling.saveInvalidPasswordLog()

  
    # Save wrong password log
    filehandling.saveWrongPasswordLog("12345")

    
    # Save invalid amount log
    filehandling.saveInvalidAmountLog("12345", "Withdraw")

if __name__ == '__main__':
    run()