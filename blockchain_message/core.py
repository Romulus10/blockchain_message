"""Provides core data types."""

class Contact(object):
    """
    """
    def __init__(self, address: str, uname: str, email: str):
        self.address = address
        self.uname = uname
        self.email = email
        with open("./keys/{0}.asc".format(uname)) as f:
            self.key = f.read()


class Message(object):
    """
    """
    def __init__(self, msg_id: int, to: Contact, fr: Contact, text: str):
        self.id = msg_id
        self.to = to
        self.fr = fr
        self.text = text
