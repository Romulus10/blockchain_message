import gpg

from src.crypt.error import KeyUnverifiedError


class Crypt(object):
    def __init__(self, email):
        self.__key = gpg.search_keys(email)[0]['keyid']

    def encrypt(self, message: str, recipients: list) -> str:
        recipient_keys = [gpg.search_keys(x)[0]['keyid'] for x in recipients]
        return gpg.encrypt(data=message, recipients=recipient_keys, sign=self._key)

    @staticmethod
    def decrypt(message: str) -> str:
        decrypt = gpg.decrypt(message)
        if decrypt.username is not None:
            return decrypt
        else:
            raise KeyUnverifiedError
