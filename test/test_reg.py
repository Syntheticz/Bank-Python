import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch
from io import StringIO
from objects import Account
from account import register, validate_name, validate_date_of_birth, validate_PIN, validate_initial_deposit



class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    @patch('builtins.input', side_effect=['John Doe', '1990-01-01', '1234', '1234', '15000'])
    def test_register(self, mock_input):
        expected_output = "Registration successful!\n"
        expected_output += "Name: John Doe\n"
        expected_output += "Date of Birth: 1990-01-01\n"
        expected_output += "PIN: 1234\n"
        expected_output += "Account Number: "
        expected_output += "Account Balance: 15000\n"

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            register(self.account)

            actual_output = mock_stdout.getvalue()
            print("Expected Output:\n", expected_output)
            print("Actual Output:\n", actual_output)

            
            self.assertEqual(self.account.name, 'John Doe')
            self.assertEqual(self.account.date_of_birth, '1990-01-01')
            self.assertEqual(self.account.PIN, '1234')
            self.assertIsNotNone(self.account.account_number)
            self.assertEqual(self.account.account_balance, '15000')

    def test_validate_name(self):
        self.assertTrue(validate_name('John Doe'))
        self.assertFalse(validate_name('1234'))
        self.assertFalse(validate_name('John123'))
        self.assertFalse(validate_name('John@Doe'))

    def test_validate_date_of_birth(self):
        self.assertTrue(validate_date_of_birth('1990-01-01'))
        self.assertFalse(validate_date_of_birth('2000-13-01'))
        self.assertFalse(validate_date_of_birth('2000-01-32'))
        self.assertFalse(validate_date_of_birth('2000-01-01T00:00:00'))

    def test_validate_PIN(self):
        self.assertTrue(validate_PIN('1234'))
        self.assertFalse(validate_PIN('12'))
        self.assertFalse(validate_PIN('12345'))
        self.assertFalse(validate_PIN('abcd'))

    def test_validate_initial_deposit(self):
        self.assertTrue(validate_initial_deposit(10000))
        self.assertTrue(validate_initial_deposit(15000))
        self.assertFalse(validate_initial_deposit(9999))



if __name__ == '__main__':
    unittest.main()
