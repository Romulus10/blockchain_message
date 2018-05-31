"""Provides OpenPGP wrappers for blockchain_message."""

import gnupg

from blockchain_message.core import Contact


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
    def __init__(self, email: str):
        """
        :param email:
        """
        self.email: str = email
        self.gpg = gnupg.GPG(
            homedir='./.keys',
            keyring='pubring.gpg',
            secring='secring.gpg'
        )

    def import_key(self, addr: str, filename: str, email: str):
        """
        Retrieves a key file, notes the fingerprint and owner, and imports it in to the
        application's keystore.
        :param addr:
        :param filename: should be the key's username
        :param email:
        :return:
        """
        return Contact(addr, filename, email)

    def encrypt(self, message: str, recipient: Contact) -> str:
        """
        :param message:
        :param recipient:
        :return:
        """
        return self.gpg.encrypt(message, recipient.key)

    def decrypt(self, message: str) -> str:
        """
        'Hello, world!'

        :param message:
        :return:
        """
        return self.gpg.decrypt(str(message))

    def sign(self, message: str) -> str:
        """
        :param message:
        :return:
        """
        pass

    def verify(self, message: str) -> str:
        """
        :param message:
        :return:
        """
        pass

    def generate_key(self, email: str):
        """
        :param email:
        :return:
        """
        self.gpg.gen_key(
            self.gpg.gen_key_input(
                name_email=email
                )
            )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
