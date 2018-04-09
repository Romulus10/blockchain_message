import shelve
from typing import List

from src.core import Contact, Message


class MessageNotFoundException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class Database (object):
    def __init__(self):
        with shelve.open("~/.blkchnmsg/db") as db:
            self.contacts: List[Contact] = db['contacts']
            self.messages: List[Message] = db['messages']

    def __pull(self):
        with shelve.open("~/.blkchnmsg/db") as db:
            self.contacts = db['contacts']
            self.messages = db['messages']

    def __commit(self):
        with shelve.open("~/.blkchnmsg/db") as db:
            db['contacts'] = self.contacts
            db['messages'] = self.messages

    def __max_msgid(self) -> int:
        m: int = 0
        for x in self.messages:
            if x.id > m:
                m = x.id
        return m

    def add_contact(self, uname: str, addr: int, email: str) -> bool:
        self.contacts.append(Contact(addr, uname, email))
        self.__commit()
        return True

    def del_contact(self, name: str) -> bool:
        for x in self.contacts:
            if x.uname is name:
                self.contacts.remove(x)
                self.__commit()
                return True
        return False

    def insert(self, to: int, fr: int, text: str) -> bool:
        self.messages.append(Message(self.__max_msgid()+1, to, fr, text))
        self.__commit()
        return True

    def delete(self, msgid: int) -> bool:
        for x in self.messages:
            if x.id is msgid:
                self.messages.remove(x)
                self.__commit()
                return True
        return False

    def read(self, msgid: int) -> Message:
        for x in self.messages:
            if x.id is msgid:
                return x
        raise MessageNotFoundException
