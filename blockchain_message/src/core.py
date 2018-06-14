"""Provides core data types."""


class Contact(object):
    """
    """

    def __init__(self, address: str, uname: str, email: str):
        """
        :param address:
        :param uname:
        :param email:
        """
        self.address = address
        self.uname = uname
        self.email = email
        with open("./.keys/{0}.pub".format(uname), 'rb') as f:
            self.key = f.read()


class Message(object):
    """
    """

    def __init__(self, msg_id: int, to: Contact, fr: Contact, text: str, sign: str):
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
        self.sign = sign
