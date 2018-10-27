import unittest

from blockchain_message.src.blockchain import Blockchain
from blockchain_message.src.core import Contact, Message


class TestChain(unittest.TestCase):
    def test_submit(self):
        b = Blockchain()
        t = Contact("0", "test", "test@test.com")
        o = Contact("1", "other", "other@test.com")
        m = Message(0, t, o, "This is a test.", '', False)
        b.submit(m)

    def test_retrieve(self):
        b = Blockchain()
        t = Contact("0", "test", "test@test.com")
        o = Contact("1", "other", "other@test.com")
        l = [t, o]
        m = Message(0, t, o, "This is a test.", '', False)
        b.submit(m)
        m = b.retrieve(t, 0, l)
        self.assertEqual(m[0].text, "This is a test.")

    def test_multiple_retrieve(self):
        b = Blockchain()
        t = Contact("0", "test", "test@test.com")
        o = Contact("1", "other", "other@test.com")
        l = [t, o]
        m = Message(0, t, o, "This is a test.", '', False)
        n = Message(1, t, o, "This is another test.", '', False)
        b.submit(m)
        b.submit(n)
        m = b.retrieve(t, 1, l)
        self.assertEqual(m[0].text, "This is another test.")
