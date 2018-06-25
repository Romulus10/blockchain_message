import shelve
from typing import List

from blockchain_message.src.core import Contact, Message


class MessageNotFoundException(Exception):
    """

    """

    def __init__(self, message):
        """

        :param message:
        """
        super().__init__(message)


class ContactNotFoundException(Exception):
    """

    """

    def __init__(self, message):
        """

        :param message:
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
            except KeyError:
                self.contacts: List[Contact] = list()
                self.messages: List[Message] = list()

    def __pull(self):
        """

        """
        with shelve.open(".blkchnmsg/db") as db:
            db.sync()
            self.contacts: List[Contact] = db['contacts']
            self.messages: List[Message] = db['messages']

    def __commit(self):
        """

        """
        with shelve.open(".blkchnmsg/db") as db:
            db['contacts']: List[Contact] = self.contacts
            db['messages']: List[Message] = self.messages
            db.sync()

    def __max_msgid(self) -> int:
        """

        :return:
        """
        m: int = -1
        for x in self.messages:
            if x.id > m:
                m = x.id
        return m

    def add_contact(self, addr: str, uname: str, email: str) -> bool:
        """
        Adds a new contact object to the database.

        :param uname:
        :param addr:
        :param email:
        :return:
        """
        self.contacts.append(Contact(addr, uname, email))
        self.__commit()
        return True

    def read_contact(self, uname: str) -> Contact:
        """

        :param uname:
        :return:
        """
        for x in self.contacts:
            if x.uname == uname:
                return x
        raise ContactNotFoundException("Contact {} does not exist.".format(uname))

    def del_contact(self, name: str) -> bool:
        """

        :param name:
        :return:
        """
        for x in self.contacts:
            if x.uname is name:
                self.contacts.remove(x)
                self.__commit()
                return True
        return False

    def insert(self, to: Contact, fr: Contact, text: str) -> int:
        """
        Produces a message object and adds it to the internal database.

        :param to:
        :param fr:
        :param text:
        :return:
        """
        self.messages.append(Message(self.__max_msgid() + 1, to, fr, text, ''))
        self.__commit()
        return self.__max_msgid()

    def delete(self, msgid: int) -> bool:
        """

        :param msgid:
        :return:
        """
        for x in self.messages:
            if x.id is msgid:
                self.messages.remove(x)
                self.__commit()
                return True
        return False

    def read(self, msgid: int) -> Message:
        """

        :param msgid:
        :return:
        """
        for x in self.messages:
            if x.id is msgid:
                return x
        raise MessageNotFoundException("Message {} not found.".format(msgid))
