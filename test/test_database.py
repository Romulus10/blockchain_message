import unittest

from blockchain_message.src.core import Contact
from blockchain_message.src.database import Database, MessageNotFoundException, ContactNotFoundException


class TestDatabase(unittest.TestCase):
    def test_insert(self):
        c0 = Contact("00000", "test", "test@test.com")
        c1 = Contact("00000", "other", "other@test.com")
        d = Database()
        r = d.insert(c0, c1, "This is a test.", '', False)
        self.assertTrue(r)

    def test_read(self):
        c0 = Contact("00000", "test", "test@test.com")
        c1 = Contact("00000", "other", "other@test.com")
        d = Database()
        r = d.insert(c0, c1, "This is a test.", '', False)
        self.assertEqual(d.read(r.id).text, "This is a test.")

    def test_delete(self):
        c0 = Contact("00000", "test", "test@test.com")
        c1 = Contact("00000", "other", "other@test.com")
        d = Database()
        r = d.insert(c0, c1, "This is a test.", '', False)
        d.delete(r.id)
        with self.assertRaises(MessageNotFoundException):
            d.read(r.id)

    def test_read_contact(self):
        d = Database()
        d.add_contact("00000", "test", "test@test.com")
        self.assertEqual(d.read_contact("test").address, "00000")

    def test_delete_contact(self):
        d = Database()
        d.add_contact("00000", "test", "test@test.com")
        d.del_contact("test")
        with self.assertRaises(ContactNotFoundException):
            d.read_contact("test")
