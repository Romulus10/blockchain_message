import gnupg

from src.core import Contact


class KeyUnverifiedError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class Crypt(object):
    def __init__(self, email: str):
        self.email = email
        self.gpg = gnupg.GPG(
            homedir='./keys',
            keyring='pubring.gpg',
            secring='secring.gpg'
        )

    def import_key(self, filename):
        """
        :param filename:
        :return:
        """
        pass

    def encrypt(self, message: str, recipient: Contact) -> str:
        """
        :param message:
        :param recipient:
        :return:
        """
        key = self.gpg.import_keys(recipient.key)
        return message

    def decrypt(self, message: str) -> str:
        """
        'Hello, world!'

        :param message:
        :return:
        """
        return message

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
