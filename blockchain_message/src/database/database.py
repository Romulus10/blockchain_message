from src.core.core import Message


class Database (object):
    def __init__(self):
        self.contacts = []
        self.messages = []

    def add_contact(self, uname: str, addr: int) -> bool:
        pass

    def del_contact(self, name: str) -> bool:
        pass

    def insert(self, msg: str) -> str:
        pass

    def delete(self, msgid: int) -> bool:
        pass

    def read(self, msgid: int) -> Message:
        pass
