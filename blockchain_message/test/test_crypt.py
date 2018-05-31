import unittest
from blockchain_message.crypt import Crypt, Contact


class TestCrypt(unittest.TestCase):
    def test_encrypt(self):
        c = Crypt("test@test.com")
        con = Contact("00000", "test", "test@test.com")

    def test_decrypt(self):
        c = Crypt("test@test.com")
        con = Contact("00000", "test", "test@test.com")
        cipher = str(c.encrypt("This is a test.", con))
        self.assertEqual(str(c.decrypt(cipher)), "This is a test.")

    def test_sign(self):
        pass

    def test_verify(self):
        pass
