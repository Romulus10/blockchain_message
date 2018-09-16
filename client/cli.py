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
    """
    for x in msg.send.contacts:
        print(x.uname)


def check(msg: BlockchainMessage, uname: str):
    """
    :param msg:
    :param uname:
    """
    n = msg.pull_messages(uname)
    print("{0} new messages.".format(n))


def write(msg: BlockchainMessage):
    """

    :param msg:
    """
    uname = input("send to: ")
    text = input("message text: ")
    msg.send_message(uname, text)


def read(msg: BlockchainMessage):
    """

    :param msg:
    """
    for x in msg.recv.messages:
        v = ":)" if x.verified else ":("
        print("{0} {1} -> {2}".format(x.fr.uname, v, x.text))


def new_contact(msg: BlockchainMessage):
    """

    :param msg:
    """
    print("Adding a new contact:")
    addr = input("addr: ")
    uname = input("uname: ")
    email = input("email: ")
    msg.send.add_contact(addr, uname, email)
    msg.recv.add_contact(addr, uname, email)


def main():
    """

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


if __name__ == "__main__":
    main()
