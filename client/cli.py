#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
blockchain_message simple client implementation.

This program is distributed with ABSOLUTELY NO WARRANTY. A copy of the GNU Public License should have been distributed
along with the source code. If not, the full text can be found at https://www.gnu.org/licenses/gpl-3.0.txt.
"""

__author__ = "Sean Batzel"
__email__ = "romulus108@protonmail.com"
__license__ = "GPL"

from blockchain_message import BlockchainMessage


def contacts(msg: BlockchainMessage):
    """
    Print the list of all registered contacts.
    :param msg: A BlockchainMessage object.
    """
    for x in msg.send.contacts:
        print(x.uname)


def check(msg: BlockchainMessage, uname: str):
    """
    Downloads all new messages for the current user.
    :param msg: A BlockchainMessage object.
    :param uname: The current user's unique username.
    """
    n = msg.pull_messages(uname)
    print("{0} new messages.".format(n))


def write(msg: BlockchainMessage):
    """
    Compose a new message.
    :param msg: A BlockchainMessage object.
    """
    uname = input("send to: ")
    text = input("message text: ")
    msg.send_message(uname, text)


def read(msg: BlockchainMessage):
    """
    Read all messages the user has received.
    :param msg: A BlockchainMessage object.
    """
    for x in msg.recv.messages:
        v = ":)" if x.verified else ":("
        print("{0} {1} -> {2}".format(x.fr.uname, v, x.text))


def new_contact(msg: BlockchainMessage):
    """
    Creates a new contact.
    :param msg: A BlockchainMessage object.
    """
    print("Adding a new contact:")
    addr = input("addr: ")
    uname = input("uname: ")
    email = input("email: ")
    msg.send.add_contact(addr, uname, email)
    msg.recv.add_contact(addr, uname, email)


def main():
    """
    Sets up the application and begins the command interpreter.
    """
    addr = input("addr > ")
    uname = input("uname > ")
    email = input("email > ")
    msg = BlockchainMessage(uname)
    msg.send.add_contact(addr, uname, email)
    msg.recv.add_contact(addr, uname, email)
    done: bool = False
    while not done:
        cmd: str = input("> ")
        if cmd == "check":
            check(msg, uname)
        if cmd == "write":
            write(msg)
        if cmd == "read":
            read(msg)
        if cmd == "contacts":
            contacts(msg)
        if cmd == "new-contact":
            new_contact(msg)
        if cmd == "exit":
            done = True
        if cmd == "help":
            print("""
            
            
            \tcheck
            \tread
            \twrite
            \tcontacts
            \tnew-contact
            \thelp
            \texit
            """)


if __name__ == "__main__":
    main()
