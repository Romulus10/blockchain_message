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
from blockchain_message import ContactNotFoundException


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
    try:
        msg.send_message(uname, text)
    except ContactNotFoundException:
        print("The requested contact doesn't exist.")


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
    uname = input("uname: ")
    email = input("email: ")
    addr = msg.get_identity(uname)
    if addr == 9999:
        print(
            "A new contact couldn't be created - the requested username doesn't exist, and the system is out of room.")
    msg.send.add_contact(addr, uname, email)
    msg.recv.add_contact(addr, uname, email)


def main():
    """
    Sets up the application and begins the command interpreter.
    """
    uname = input("uname > ")
    email = input("email > ")
    password = input("password > ")
    msg = BlockchainMessage(uname)
    addr = msg.get_my_identity(uname, password)
    if addr == 9999:
        print(
            "A new contact couldn't be created - the requested username doesn't exist, and the system is out of room.")
        main()
    if addr == 99999:
        print("The password for the given user was incorrect.")
        main()
    if addr == 999999:
        print("The given user is connected to a different device.")
        main()
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
        if cmd == "balance":
            print(msg.get_balance())
        if cmd == "exit":
            done = True
        if cmd == "help":
            print(""" blckchnmsg is a command-line utility for sending short email-like messages over Ethereum.
            
            This program is distributed with ABSOLUTELY NO WARRANTY. A copy of the GNU Public License should have been distributed
along with the source code. If not, the full text can be found at https://www.gnu.org/licenses/gpl-3.0.txt.
            
            
            \tbalance - Check the Ethereum account's balance.
            \tcheck - See if any new messages have been received.
            \tread - Read all of the messages we've already downloaded.
            \twrite - Compose and send a new message.
            \tcontacts - List the system's current contacts.
            \tnew-contact - Create a new contact object.
            \thelp - Display this help dialog.
            \texit - ALWAYS use this to end the program. It's responsible for making sure everything saves right.
            """)


if __name__ == "__main__":
    main()
