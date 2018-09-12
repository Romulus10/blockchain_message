"""Provides core data types."""


class Contact(object):
    """
    Abstracts handling contact information.
    """

    def __init__(self, address: str, uname: str, email: str):
        """
        Produces an object to store information for the given contact and associates their public key.
        :param address: The unique identifying number for the contact.
        :param uname: The unique username for the contact.
        :param email: The contact's given email address.
        """
        self.address = address
        self.uname = uname
        self.email = email
        with open("./.keys/{0}.pub".format(uname), 'rb') as f:
            self.key = f.read()


class Message(object):
    """
    Object to store all information necessary for processing messages.
    """

    def __init__(self, msg_id: int, to: Contact, fr: Contact, text: str, sign: str, verified: bool):
        """
        :param msg_id: The unique identifying number for the message.
        :param to: The ID of the recipient.
        :param fr: The ID of the sender.
        :param text: The text of the message.
        """
        self.id = msg_id
        self.to = to
        self.fr = fr
        self.text = text
        self.sign = sign
        self.verified = verified
