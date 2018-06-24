from blockchain_message.src.database import Database
from blockchain_message.src.crypt import Crypt
from blockchain_message.src.blockchain import Blockchain
from blockchain_message.src.core import Message


class BlockchainMessage(object):
    """

    """
    def __init__(self, uname: str):
        """

        :param uname:
        """
        self.d = Database()
        self.c = Crypt(uname)
        self.b = Blockchain()

    def pull_messages(self, uname: str) -> int:
        """
        :return: The number of new messages returned from the blockchain.
        """
        n = 0
        m = self.b.retrieve(self.d.read_contact(uname), len(self.d.messages), self.d.contacts)
        for g in m:
            self.c.verify(g.text, g.sign, g.fr)
            g.text = self.c.decrypt(bytes(g.text))
            self.d.insert(g.to, g.fr, g.text)
            n += 1
        return n

    def send_message(self, uname: str, text: str):
        """
        :param uname:
        :param text:
        :return:
        """
        t_c = self.c.encrypt(text, self.d.read_contact(uname))
        self.b.submit(Message(0, self.d.read_contact(uname),
                              self.d.read_contact(uname),
                              str(t_c),
                              str(self.c.sign(str(t_c)))))
