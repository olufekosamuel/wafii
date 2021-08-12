import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import unittest
from app import Wafi


wafi_test = Wafi()

class BaseCase(unittest.TestCase):
    def test_add_user_success(self):
        actual = wafi_test.add_user(user="User O")
        self.assertIsNotNone(actual)

    def test_deposit_money(self):
        actual = wafi_test.deposit_money(user="User O", amount=40000)
        self.assertIsNotNone(actual)

    def test_transfer_money(self):
        actual = wafi_test.transfer_money(sender="User O", receiver="User X", amount=400)
        self.assertIsNotNone(actual)

    def test_check_balance(self):
        actual = wafi_test.check_balance(user="User O")
        self.assertIsNotNone(actual)

if __name__ == '__main__':
    unittest.main()