import unittest

from sys import  path

from pathlib import Path
import os
path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from objects import Account
from filehandling import *


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

class EncryptionTestCase(unittest.TestCase):

    def test_swap_chars(self):
        
        # Test encryption with key=3
        self.assertEqual(swap_chars("Hello World!", 3), "Khoor#Zruog$")
        self.assertEqual(swap_chars("12345", 3), "45678")
        self.assertEqual(swap_chars("!@#$%^&*()", 3), "$C&'(a)-+,")
        self.assertEqual(swap_chars("Lorem Ipsum", 3), "Oruhp#Lsvxp")
        self.assertEqual(swap_chars("Python Programming", 3), "S|wkrq#Surjudpplqj")
        self.assertEqual(swap_chars("abcdefghijklmnopqrstuvwxyz", 3), "defghijklmnopqrstuvwxyz{|}")
        self.assertEqual(swap_chars("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3), "DEFGHIJKLMNOPQRSTUVWXYZ[\]")
        self.assertEqual(swap_chars("0123456789", 3), "3456789:;<")

        # Test encryption with key=-5
      

    def test_restore_chars(self):
        self.assertEqual(restore_chars("Khoor#Zruog$", 3), "Hello World!")
        self.assertEqual(restore_chars("45678", 3), "12345")
        self.assertEqual(restore_chars("$C&'(a)-+,", 3), "!@#$%^&*()")
        self.assertEqual(restore_chars("Oruhp#Lsvxp", 3), "Lorem Ipsum")
        self.assertEqual(restore_chars("S|wkrq#Surjudpplqj", 3), "Python Programming")
        self.assertEqual(restore_chars("defghijklmnopqrstuvwxyz{|}", 3), "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(restore_chars("DEFGHIJKLMNOPQRSTUVWXYZ[\]", 3), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(restore_chars("3456789:;<", 3), "0123456789")

    def test_encrypt_decimal(self):
        
        # Test decimal encryption
        self.assertEqual(encrypt_decimal(5651.562231275058, 5), ":;:6:;")
        self.assertEqual(encrypt_decimal(5729.016370211528, 5), ":<7>57")
        self.assertEqual(encrypt_decimal(8432.580435228854, 5), "=987:=")
        self.assertEqual(encrypt_decimal(454.153012636932, 5), "9:96:")
        self.assertEqual(encrypt_decimal(2284.4419356502353, 5), "77=999")
        self.assertEqual(encrypt_decimal(4516.245003961823, 5), "9:6;7:")
        self.assertEqual(encrypt_decimal(3183.562741668744, 5), "86=8:;")
        self.assertEqual(encrypt_decimal(1127.1112906991177, 5), "667<66")
        self.assertEqual(encrypt_decimal(8139.098306904809, 5), "=68>65")
        self.assertEqual(encrypt_decimal(900.9908110574394, 5), ">55>>")
        self.assertEqual(encrypt_decimal(7582.8651746309315, 5), "<:=7=<")
        self.assertEqual(encrypt_decimal(9207.550401250039, 5), ">75<::")
        self.assertEqual(encrypt_decimal(4207.25847574597, 5), "975<7;")
        self.assertEqual(encrypt_decimal(3970.9696705228725, 5), "8><5><")
        self.assertEqual(encrypt_decimal(9408.792784162886, 5), ">95=<>")
        self.assertEqual(encrypt_decimal(8894.813403985921, 5), "==>9=6")
        self.assertEqual(encrypt_decimal(8203.625627863003, 5), "=758;8")
        self.assertEqual(encrypt_decimal(3450.114184454095, 5), "89:566")
        self.assertEqual(encrypt_decimal(2641.493265886712, 5), "7;969>")
        self.assertEqual(encrypt_decimal(5939.362863878291, 5), ":>8>8;")
        self.assertEqual(encrypt_decimal(4159.163947751166, 5), "96:>6;")
        self.assertEqual(encrypt_decimal(6651.161360139211, 5), ";;:66;")
        self.assertEqual(encrypt_decimal(7192.730270731073, 5), "<6>7<8")
        self.assertEqual(encrypt_decimal(6597.972869302078, 5), ";:><><")
        self.assertEqual(encrypt_decimal(4659.459505822332, 5), "9;:>9;")
        self.assertEqual(encrypt_decimal(2651.5034944946624, 5), "7;:6:5")
        self.assertEqual(encrypt_decimal(2114.1210102691866, 5), "766967")
        self.assertEqual(encrypt_decimal(4118.795645170493, 5), "966==5")
        self.assertEqual(encrypt_decimal(8221.766173064241, 5), "=776<<")
        self.assertEqual(encrypt_decimal(3827.740731522671, 5), "8=7<<9")
        self.assertEqual(encrypt_decimal(1072.388393966449, 5), "65<78>")
        self.assertEqual(encrypt_decimal(849.8660782602818, 5), "=9>=<")
        self.assertEqual(encrypt_decimal(3649.9581745711184, 5), "8;9>>;")
        self.assertEqual(encrypt_decimal(9630.165507483825, 5), ">;856<")
        self.assertEqual(encrypt_decimal(6006.607255134418, 5), ";55;;6")
        self.assertEqual(encrypt_decimal(2945.237820224875, 5), "7>9:79")
        self.assertEqual(encrypt_decimal(4312.732670414735, 5), "9867<8")
        self.assertEqual(encrypt_decimal(2431.794996971095, 5), "7986<>")
        self.assertEqual(encrypt_decimal(4899.418790382915, 5), "9=>>97")
        self.assertEqual(encrypt_decimal(8528.959337173323, 5), "=:7=>;")
        self.assertEqual(encrypt_decimal(4357.515589645238, 5), "98:<:7")
        self.assertEqual(encrypt_decimal(1480.3630039332572, 5), "69=58;")
        self.assertEqual(encrypt_decimal(4685.85477638494, 5), "9;=:=:")
        self.assertEqual(encrypt_decimal(1943.9541090007017, 5), "6>98>:")
        self.assertEqual(encrypt_decimal(1967.8979846797652, 5), "6>;<>5")
        self.assertEqual(encrypt_decimal(9138.778270485176, 5), ">68=<=")
        self.assertEqual(encrypt_decimal(127.5364697575021, 5), "67<:9")
        self.assertEqual(encrypt_decimal(8683.545800414844, 5), "=;=8::")
        self.assertEqual(encrypt_decimal(5739.0846617096095, 5), ":<8>5=")
        self.assertEqual(encrypt_decimal(3885.9684276028383, 5), "8==:><")

    def test_decrypt_decimal(self):
        # Test decimal decryption
        self.assertEqual(decrypt_decimal(";:<75:", 5), 6572.05)
        self.assertEqual(decrypt_decimal(">>7;;7", 5), 9926.62)
        self.assertEqual(decrypt_decimal(">;:985", 5), 9654.3)
        self.assertEqual(decrypt_decimal("6>66>", 5), 191.19)
        self.assertEqual(decrypt_decimal(";>=96;", 5), 6984.16)
        self.assertEqual(decrypt_decimal("<5>5", 5), 70.9)
        self.assertEqual(decrypt_decimal(";7<7=8", 5), 6272.83)
        self.assertEqual(decrypt_decimal("85<>8=", 5), 3079.38)
        self.assertEqual(decrypt_decimal("<6:98<", 5), 7154.37)
        self.assertEqual(decrypt_decimal(";<5576", 5), 6700.21)
        self.assertEqual(decrypt_decimal("889>9>", 5), 3349.49)
        self.assertEqual(decrypt_decimal("87;>59", 5), 3269.04)
        self.assertEqual(decrypt_decimal("=:=988", 5), 8584.33)
        self.assertEqual(decrypt_decimal(";;<5:>", 5), 6670.59)
        self.assertEqual(decrypt_decimal("=;96>:", 5), 8641.95)
        self.assertEqual(decrypt_decimal("9:598", 5), 450.43)
        self.assertEqual(decrypt_decimal(":9559:", 5), 5400.45)
        self.assertEqual(decrypt_decimal(":;>85:", 5), 5693.05)
        self.assertEqual(decrypt_decimal("<:979<", 5), 7542.47)
        self.assertEqual(decrypt_decimal("786:<9", 5), 2315.74)
        self.assertEqual(decrypt_decimal("9<97=<", 5), 4742.87)
        self.assertEqual(decrypt_decimal("=;;988", 5), 8664.33)
        self.assertEqual(decrypt_decimal("9777>:", 5), 4222.95)
        self.assertEqual(decrypt_decimal(";65665", 5), 6101.1)
        self.assertEqual(decrypt_decimal(":9>=<:", 5), 5498.75)
        self.assertEqual(decrypt_decimal("98;9;8", 5), 4364.63)
        self.assertEqual(decrypt_decimal(";8>85", 5), 639.3)
        self.assertEqual(decrypt_decimal("=7=7<6", 5), 8282.71)
        self.assertEqual(decrypt_decimal(">5>>=8", 5), 9099.83)
        self.assertEqual(decrypt_decimal(";;;895", 5), 6663.4)
        self.assertEqual(decrypt_decimal(":=:689", 5), 5851.34)
        self.assertEqual(decrypt_decimal("<9>=97", 5), 7498.42)
        self.assertEqual(decrypt_decimal("7;=6<6", 5), 2681.71)
        self.assertEqual(decrypt_decimal("=:766:", 5), 8521.15)
        self.assertEqual(decrypt_decimal("=6;665", 5), 8161.1)
        self.assertEqual(decrypt_decimal("9>::<8", 5), 4955.73)
        self.assertEqual(decrypt_decimal(":<<;;:", 5), 5776.65)
        self.assertEqual(decrypt_decimal(">===;5", 5), 9888.6)
        self.assertEqual(decrypt_decimal("786698", 5), 2311.43)
        self.assertEqual(decrypt_decimal("9:6<>:", 5), 4517.95)
        self.assertEqual(decrypt_decimal(":7=69", 5), 528.14)
        self.assertEqual(decrypt_decimal("<>8=79", 5), 7938.24)
        self.assertEqual(decrypt_decimal("96=;86", 5), 4186.31)
        self.assertEqual(decrypt_decimal("86;==:", 5), 3168.85)
        self.assertEqual(decrypt_decimal("856=<=", 5), 3018.78)
        self.assertEqual(decrypt_decimal(":5;6;<", 5), 5061.67)
        self.assertEqual(decrypt_decimal("7;6755", 5), 2612.0)
        self.assertEqual(decrypt_decimal("9756:8", 5), 4201.53)
        self.assertEqual(decrypt_decimal(";7;586", 5), 6260.31)
        self.assertEqual(decrypt_decimal(";=59:7", 5), 6804.52)

 
    def test_encrypt_decrypt_account(self):
        # Test data
        account = ACCOUNT("1234567890", "John Doe", "1990-01-01", "1234", "0", 5000.0, True)
        key = 5

        # Encrypt the account
        encrypt_account(account, key)

        # Check if encryption is successful
        self.assertNotEqual(account.name, "John Doe")
        self.assertNotEqual(account.account_number, "1234567890")
        self.assertNotEqual(account.date_of_birth, "1990-01-01")
        self.assertNotEqual(account.PIN, "1234")
        self.assertNotEqual(account.encrypted_account_bal, "0")
        self.assertNotEqual(account.account_balance, 5000.0)

        # Decrypt the account
        decrypt_account(account, key)

        # Check if decryption is successful
        self.assertEqual(account.name, "John Doe")
        self.assertEqual(account.account_number, "1234567890")
        self.assertEqual(account.date_of_birth, "1990-01-01")
        self.assertEqual(account.PIN, "1234")
        self.assertEqual(account.account_balance, 5000.0)
        self.assertEqual(account.encrypted_account_bal, "0")



if __name__ == '__main__':
    unittest.main()

    main.run()
    
