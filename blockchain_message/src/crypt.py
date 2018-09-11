"""Provides OpenPGP wrappers for blockchain_message."""

import rsa

from blockchain_message.src.core import Contact


class KeyUnverifiedError(Exception):
    """
    """

    def __init__(self, message: str, errors: str):
        """
        :param message:
        :param errors:
        """
        super().__init__(message)
        self.errors = errors


class Crypt(object):
    """
    """

    def __init__(self, uname: str):
        """
        :param uname:
        """
        try:
            with open('./.keys/{0}.priv'.format(uname), 'rb') as f:
                self.key = rsa.PrivateKey.load_pkcs1(f.read())
        except ValueError:
            self.generate_key(uname)
            with open('./.keys/{0}.priv'.format(uname), 'rb') as f:
                self.key = rsa.PrivateKey.load_pkcs1(f.read())
        except FileNotFoundError:
            self.generate_key(uname)
            with open('./.keys/{0}.priv'.format(uname), 'rb') as f:
                self.key = rsa.PrivateKey.load_pkcs1(f.read())

    @staticmethod
    def import_key(addr: str, filename: str, email: str):
        """
        Retrieves a key file, notes the fingerprint and owner, and imports it in to the
        application's keystore.
        :param addr:
        :param filename: should be the key's username
        :param email:
        :return:
        """
        return Contact(addr, filename, email)

    @staticmethod
    def encrypt(message: str, recipient: Contact) -> bytes:
        """
        :param message:
        :param recipient:
        :return:
        """
        return rsa.encrypt(message.encode('latin-1'),
                           rsa.PublicKey.load_pkcs1(recipient.key))

    def decrypt(self, message: bytes) -> str:
        """
        'Hello, world!'

        :param message:
        :return:
        """
        return rsa.decrypt(message, self.key).decode('latin-1')

    def sign(self, message: str) -> str:
        """
        :param message:
        :return:
        """
        return rsa.sign(message.encode('latin-1'), self.key, 'SHA-1')

    @staticmethod
    def verify(message: str, signature: str, sender: Contact) -> str:
        """
        :param message:
        :param signature:
        :param sender:
        :return:
        """
        m = bytes(bytes(message, 'latin-1').decode('latin-1'), 'latin-1')
        s = bytes(bytes(signature, 'latin-1').decode('latin-1'), 'latin-1')
        return rsa.verify(m, s, rsa.PublicKey.load_pkcs1(sender.key))

    @staticmethod
    def generate_key(uname: str):
        """
        :param uname:
        :return:
        """
        (pubkey, privkey) = rsa.newkeys(2048, poolsize=8)
        with open('./.keys/{0}.priv'.format(uname), 'wb') as f:
            f.write(privkey.save_pkcs1('PEM'))
        with open('./.keys/{0}.pub'.format(uname), 'wb') as f:
            f.write(pubkey.save_pkcs1('PEM'))
