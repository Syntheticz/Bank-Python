import unittest

from sys import  path

from pathlib import Path
import os
path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from objects import Account
from filehandling import save, retrieve_by_account_number, overwrite_record


#Actual Components
import main


class TestCreateAndRead(unittest.TestCase):
    def setUp(self):
        self.filepath = "test_accounts.txt"

    def tearDown(self):
        if Path(self.filepath).is_file():
            Path(self.filepath).unlink()

    def test_save_and_retrieve(self):
        account1 = Account("1234567890", "John Doe", "1990-01-01", "1234", "encrypted", 1000.0, True)
        account2 = Account("9876543210", "Jane Smith", "1995-05-10", "5678", "encrypted", 2000.0, True)

        save(self.filepath, account1)
        save(self.filepath, account2)

        retrieved1 = retrieve_by_account_number(self.filepath, "1234567890")
        retrieved2 = retrieve_by_account_number(self.filepath, "9876543210")

        self.assertEqual(account1.account_number, retrieved1.account_number)
        self.assertEqual(account1.name, retrieved1.name)
        self.assertEqual(account2.account_number, retrieved2.account_number)
        self.assertEqual(account2.name, retrieved2.name)

    def test_overwrite_record(self):
        account1 = Account("1234567890", "John Doe", "1990-01-01", "1234", "encrypted", 1000.0, True)
        account2 = Account("1234567890", "Jane Smith", "1995-05-10", "5678", "encrypted", 2000.0, True)

        save(self.filepath, account1)
        overwrite_record(self.filepath, account1, account2)

        retrieved = retrieve_by_account_number(self.filepath, "1234567890")

        self.assertEqual(account2.name, retrieved.name)




if __name__ == '__main__':
    unittest.main()

    main.run()
    
