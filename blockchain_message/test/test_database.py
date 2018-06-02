import unittest

from blockchain_message.src.core import Contact
from blockchain_message.src.database import Database, MessageNotFoundException, ContactNotFoundException


class TestDatabase(unittest.TestCase):
    def test_insert(self):
        c0 = Contact("00000", "test", "test@test.com")
        c1 = Contact("00000", "other", "other@test.com")
        d = Database()
        r = d.insert(c0, c1, "This is a test.")
        self.assertTrue(r)

    def test_read(self):
        c0 = Contact("00000", "test", "test@test.com")
        c1 = Contact("00000", "other", "other@test.com")
        d = Database()
        r = d.insert(c0, c1, "This is a test.")
        self.assertEqual(d.read(r).text, "This is a test.")

    def test_delete(self):
        c0 = Contact("00000", "test", "test@test.com")
        c1 = Contact("00000", "other", "other@test.com")
        d = Database()
        r = d.insert(c0, c1, "This is a test.")
        d.delete(r)
        with self.assertRaises(MessageNotFoundException):
            d.read(r)

    def test_read_contact(self):
        d = Database()
        d.add_contact("test", "00000", "test@test.com")
        self.assertEqual(d.read_contact("test").address, "00000")

    def test_delete_contact(self):
        d = Database()
        d.add_contact("test", "00000", "test@test.com")
        d.del_contact("test")
        with self.assertRaises(ContactNotFoundException):
            d.read_contact("test")
