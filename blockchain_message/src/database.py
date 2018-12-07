import shelve
from typing import List

from blockchain_message.src.core import Contact, Message


class MessageNotFoundException(Exception):
    """
    Thrown when a message matching an ID does not exist in the database.
    """

    def __init__(self, message):
        """
        Default constructor.
        :param message: The text of the exception detail.
        """
        super().__init__(message)


class ContactNotFoundException(Exception):
    """
    Thrown when a Contact database query fails.
    """

    def __init__(self, message):
        """
        Default constructor.
        :param message: Exception detail text.
        """
        super().__init__(message)


class Database(object):
    def __init__(self):
        """

        """
        with shelve.open(".blkchnmsg/db") as db:
            try:
                self.contacts: List[Contact] = db['contacts']
                self.messages: List[Message] = db['messages']
                self.max_msgid: int = db['max_msg']
            except KeyError:
                self.contacts: List[Contact] = list()
                self.messages: List[Message] = list()
                self.max_msgid: int = 0

    def __pull(self):
        """

        """
        with shelve.open(".blkchnmsg/db") as db:
            db.sync()
            self.contacts: List[Contact] = db['contacts']
            self.messages: List[Message] = db['messages']
            self.max_msgid: int = db['max_msg']

    def __commit(self):
        """

        """
        with shelve.open(".blkchnmsg/db") as db:
            db['contacts']: List[Contact] = self.contacts
            db['messages']: List[Message] = self.messages
            db['max_msg']: int = self.max_msgid
            db.sync()

    def __max_msgid(self) -> int:
        """

        :return: The current maximum message ID.
        """
        m: int = -1
        for x in self.messages:
            if x.id > m:
                m = x.id
        self.max_msgid = m
        return m

    def add_contact(self, addr: str, uname: str, email: str) -> bool:
        """
        Adds a new contact object to the database.

        :param uname: The contact's uname.
        :param addr: The address retrieved from the Identity Manager contract.
        :param email: The contact's email address, used to verify correct identity.
        :return: Whether or not the contact was created successfully.
        """
        self.contacts.append(Contact(addr, uname, email))
        self.__commit()
        return True

    def read_contact(self, uname: str) -> Contact:
        """

        :param uname: The username to read data for.
        :return: The Contact object associated with the given username.
        """
        for x in self.contacts:
            if x.uname == uname:
                return x
        raise ContactNotFoundException("Contact {} does not exist.".format(uname))

    def del_contact(self, name: str) -> bool:
        """

        :param name: The uname of the contact to be deleted.s
        :return: Was the deletion successful?
        """
        for x in self.contacts:
            if x.uname is name:
                self.contacts.remove(x)
                self.__commit()
                return True
        return False

    def insert(self, to: Contact, fr: Contact, text: str, sign: str, verified: bool) -> Message:
        """
        Produces a message object and adds it to the internal database.

        :param to: The Contact the message is being sent to.
        :param fr: The Contact the message originated from.
        :param text: The text of the message itself.
        :param sign: The cryptographic signature of the unencrypted message text.
        :param verified: Whether or not the message's signature has been verified successfully.
        :return: The message object that has just been added to the database.
        """
        m = Message(self.__max_msgid() + 1, to, fr, text, sign, verified)
        self.messages.append(m)
        self.__commit()
        return m

    def delete(self, msgid: int) -> bool:
        """

        :param msgid: The ID of the message to delete.
        :return: Deleted successfully?
        """
        for x in self.messages:
            if x.id is msgid:
                self.messages.remove(x)
                self.__commit()
                return True
        return False

    def read(self, msgid: int) -> Message:
        """

        :param msgid: The ID of the message to read.
        :return: The message corresponding to msgid.
        """
        for x in self.messages:
            if x.id is msgid:
                return x
        raise MessageNotFoundException("Message {} not found.".format(msgid))

    def message_index(self) -> int:
        """
        :return: The highest current message index.
        """
        return self.__max_msgid()
