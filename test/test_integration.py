import unittest

from blockchain_message.src import *


class IntegrationTest(unittest.TestCase):
    def test_send_receive(self):
        c = Crypt('test')
        b = Blockchain()
        d = Database()
        d.add_contact('00000', 'test', 'test@test.com')
        d.add_contact('00001', 'other', 'other@test.com')
        t = "This is a test."
        t_c = c.encrypt(t, d.read_contact('test'))
        b.submit(Message(0, d.read_contact('test'), d.read_contact('test'), str(t_c), str(c.sign(str(t_c))), False))
        m = b.retrieve(d.read_contact('test'), 0, d.contacts)
        for g in m:
            c.verify(g.text, g.sign, g.fr)
            g.text = c.decrypt(bytes(g.text))
            d.insert(g.to, g.fr, g.text, '', False)
        self.assertEqual(d.read(len(d.messages) - 1).text, "This is a test.")
