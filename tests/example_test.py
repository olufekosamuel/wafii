import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import unittest
from app import Wafi


wafi_test = Wafi()

class BaseCase(unittest.TestCase):
    def test_add_user_a_success(self): #user A is added to the app
        actual = wafi_test.add_user(user="User A")
        self.assertIsNotNone(actual)

    def test_user_a_deposit_money(self): #user A is deposits 10 dollars to the app
        actual = wafi_test.deposit_money(user="User A", amount=10)
        self.assertIsNotNone(actual)

    def test_add_user_b_success(self): #user B is added to the app
        actual = wafi_test.add_user(user="User B")
        self.assertIsNotNone(actual)

    def test_user_b_deposit_money(self): #user B is deposits 20 dollars to the app
        actual = wafi_test.deposit_money(user="User B", amount=20)
        self.assertIsNotNone(actual)

    def test_user_b_to_user_a_transfer_money(self): #user B transfers 15 dollars from user B to user A
        actual = wafi_test.transfer_money(sender="User B", receiver="User A", amount=15)
        self.assertIsNotNone(actual)

    def test_user_a_check_balance(self):  #user A checks balance
        actual = wafi_test.check_balance(user="User A")
        self.assertIsNotNone(actual)

    def test_user_b_check_balance(self): #user B checks balance
        actual = wafi_test.check_balance(user="User B")
        self.assertIsNotNone(actual)

    def ztest_user_a_to_user_b_transfer_money(self): #user transfers 15 dollars from user B to user A
        actual = wafi_test.transfer_money(sender="User A", receiver="User B", amount=25)
        self.assertIsNotNone(actual)
    
    def test_check_balance_user_a(self): #user A checks balance
        actual = wafi_test.check_balance(user="User A")
        self.assertIsNotNone(actual)

if __name__ == '__main__':
    unittest.main()