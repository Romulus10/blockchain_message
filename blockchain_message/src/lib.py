import rsa

from blockchain_message.src.blockchain import Blockchain
from blockchain_message.src.crypt import Crypt
from blockchain_message.src.database import Database


class BlockchainMessage(object):
    """
    Wrapper functions that abstract access to the library itself.
    """

    def __init__(self, uname: str):
        """
        Application constructor that creates new objects for the system's functionality.
        :param uname: The currently logged-in user's unique username.
        """
        self.uname = uname
        self.recv = Database()
        self.send = Database()
        self.c = Crypt(uname)
        self.b = Blockchain()

    def get_identity(self, uname) -> int:
        """

        :param uname:
        :return:
        """
        return self.b.get_identity(uname)

    def get_balance(self) -> float:
        """

        :return:
        """
        return self.b.get_balance()

    def pull_messages(self, uname: str) -> int:
        """
        Downloads all new messages for the current user from the smart contract.
        :param uname: The currently logged-in user's unique username.
        :return: The number of new messages returned from the blockchain.
        """
        n = 0
        m = self.b.retrieve(self.recv.read_contact(uname), self.recv.message_index() + 1, self.recv.contacts)
        for g in m:
            g.text = self.c.decrypt(bytes(g.text, 'latin-1'))
            try:
                self.c.verify(g.text, g.sign, g.fr)
                v = True
            except rsa.pkcs1.VerificationError:
                v = False
            self.recv.insert(g.to, g.fr, g.text, '', v)
            n += 1
        return n

    def send_message(self, uname: str, text: str):
        """
        Encode and upload a new message to be sent to a contact.
        :param uname: The username for the intended recipient of the message.
        :param text: The text of the message being sent.
        """
        t_s = self.c.sign(str(text))
        t_c = self.c.encrypt(text, self.recv.read_contact(uname)).decode('latin-1')
        m = self.send.insert(self.send.read_contact(uname), self.send.read_contact(self.uname), t_c, t_s, True)
        self.b.submit(m)
