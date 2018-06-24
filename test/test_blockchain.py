import unittest

from blockchain_message.src.blockchain import Blockchain
from blockchain_message.src.core import Contact, Message


class TestChain(unittest.TestCase):
    def test_submit(self):
        b = Blockchain()
        t = Contact("00000", "test", "test@test.com")
        o = Contact("00001", "other", "other@test.com")
        m = Message(0, t, o, "This is a test.", '')

    def test_retrieve(self):
        b = Blockchain()
        t = Contact("00000", "test", "test@test.com")
        o = Contact("00001", "other", "other@test.com")
        l = [t, o]
        m = Message(0, t, o, "This is a test.", '')
        b.submit(m)
        m = b.retrieve(t, 0, l)
        self.assertEqual(m[0].text, "This is a test.")
