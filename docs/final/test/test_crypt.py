import unittest

from blockchain_message.src.crypt import Crypt, Contact


class TestCrypt(unittest.TestCase):
    def test_encrypt(self):
        c = Crypt("test")
        con = Contact("00000", "test", "test@test.com")
        cipher = c.encrypt("This is a test.", con)

    def test_decrypt(self):
        c = Crypt("test")
        con = Contact("00000", "test", "test@test.com")
        cipher = c.encrypt("This is a test.", con)
        self.assertEqual(str(c.decrypt(cipher)), "This is a test.")

    def test_sign(self):
        c = Crypt("other")
        con = Contact("00001", "other", "other@test.com")
        signature = c.sign("This is a test.")

    def test_verify(self):
        c = Crypt("other")
        con = Contact("00001", "other", "other@test.com")
        message = "This is a test."
        signature = str(c.sign(message))
        c.verify(message, signature, con)
