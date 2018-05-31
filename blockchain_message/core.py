"""Provides core data types."""

import gnupg


class Contact(object):
    """
    """
    def __init__(self, address: str, uname: str, email: str):
        """
        :param address:
        :param uname:
        :param email:
        """
        gpg = gnupg.GPG(
            homedir='./.keys',
            keyring='pubring.gpg',
            secring='secring.gpg'
        )
        self.address = address
        self.uname = uname
        self.email = email
        with open("./.keys/{0}.asc".format(uname)) as f:
            self.key = gpg.import_keys(f.read()).results[0]['fingerprints'][0]


class Message(object):
    """
    """
    def __init__(self, msg_id: int, to: Contact, fr: Contact, text: str):
        """
        :param msg_id:
        :param to:
        :param fr:
        :param text:
        """
        self.id = msg_id
        self.to = to
        self.fr = fr
        self.text = text


if __name__ == '__main__':
    import doctest
    doctest.testmod()
