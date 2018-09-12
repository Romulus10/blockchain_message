"""Provides OpenPGP wrappers for blockchain_message."""

import rsa

from blockchain_message.src.core import Contact


class Crypt(object):
    """
    Wrapper for Python's RSA module to simplify working with public key cryptography.
    """

    def __init__(self, uname: str):
        """
        Configures the application to use the correct private key.
        :param uname: The current username.
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
        :param addr: The user's identifying ID number.
        :param filename: Should be the key's username.
        :param email: The email address associated with the user.
        :return: A new contact object with a connected public key.
        """
        return Contact(addr, filename, email)

    @staticmethod
    def encrypt(message: str, recipient: Contact) -> bytes:
        """
        Carries out RSA encryption.
        :param message: The message to be encrypted.
        :param recipient: The individual whose public key to encrypt with.
        :return: A bytestring representing the encrypted message.
        """
        return rsa.encrypt(message.encode('latin-1'),
                           rsa.PublicKey.load_pkcs1(recipient.key))

    def decrypt(self, message: bytes) -> str:
        """
        Carries out decryption on a given bytestring using the current private key.
        :param message: The message to decrypt.
        :return: A plaintext message decrypted from 'message'.
        """
        return rsa.decrypt(message, self.key).decode('latin-1')

    def sign(self, message: str) -> str:
        """
        Applies a cryptographic signature to the given message.
        :param message: The message to sign.
        :return: The cryptographic signature for the given payload.
        """
        return rsa.sign(message.encode('latin-1'), self.key, 'SHA-1')

    @staticmethod
    def verify(message: str, signature: str, sender: Contact):
        """
        Verifies the validity of a given signature for the given contact.
        :param message: The message to verify.
        :param signature: The signature to verify.
        :param sender: The contact who the message claims to be sent by.
        """
        m = bytes(bytes(message, 'latin-1').decode('latin-1'), 'latin-1')
        s = bytes(bytes(signature, 'latin-1').decode('latin-1'), 'latin-1')
        rsa.verify(m, s, rsa.PublicKey.load_pkcs1(sender.key))

    @staticmethod
    def generate_key(uname: str):
        """
        Produces a new keypair for encryption.
        :param uname: The user's chosen username - this will be used as the key's filename.
        """
        (pubkey, privkey) = rsa.newkeys(2048, poolsize=8)
        with open('./.keys/{0}.priv'.format(uname), 'wb') as f:
            f.write(privkey.save_pkcs1('PEM'))
        with open('./.keys/{0}.pub'.format(uname), 'wb') as f:
            f.write(pubkey.save_pkcs1('PEM'))
