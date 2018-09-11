import rsa

from blockchain_message.src.blockchain import Blockchain
from blockchain_message.src.crypt import Crypt
from blockchain_message.src.database import Database


class BlockchainMessage(object):
    """

    """

    def __init__(self, uname: str):
        """

        :param uname:
        """
        self.uname = uname
        self.recv = Database()
        self.send = Database()
        self.c = Crypt(uname)
        self.b = Blockchain()

    def pull_messages(self, uname: str) -> int:
        """
        :return: The number of new messages returned from the blockchain.
        """
        n = 0
        m = self.b.retrieve(self.recv.read_contact(uname), self.recv.message_index() + 1, self.recv.contacts)
        for g in m:
            try:
                self.c.verify(g.text, g.sign, g.fr)
                v = True
            except rsa.pkcs1.VerificationError:
                v = False
            g.text = self.c.decrypt(bytes(g.text, 'latin-1'))
            self.recv.insert(g.to, g.fr, g.text, '', v)
            n += 1
        return n

    def send_message(self, uname: str, text: str):
        """
        :param uname:
        :param text:
        :return:
        """
        t_c = self.c.encrypt(text, self.recv.read_contact(uname)).decode('latin-1')
        t_s = self.c.sign(str(t_c))
        m = self.send.insert(self.send.read_contact(uname), self.send.read_contact(self.uname), t_c, t_s, True)
        self.b.submit(m)
