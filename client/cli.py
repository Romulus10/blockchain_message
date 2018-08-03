#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
blockchain_message simple client implementation.

This program is distributed with ABSOLUTELY NO WARRANTY. A copy of the GNU Public License should have been distributed
along with the source code. If not, the full text can be found at https://www.gnu.org/licenses/gpl-3.0.txt.
"""

__version__ = "0.1.0"

__author__ = "Sean Batzel"
__email__ = "romulus108@protonmail.com"
__license__ = "GPL"


from blockchain_message.src.lib import BlockchainMessage


def contacts(msg: BlockchainMessage):
    """
    :return:
    """
    for x in msg.d.contacts:
        print(x.uname)


def check(msg: BlockchainMessage, uname: str):
    """
    :param msg:
    :param uname:
    :return:
    """
    n = msg.pull_messages(uname)
    print("{0} new messages.".format(n))


def write(msg: BlockchainMessage):
    """

    :param msg:
    :return:
    """
    uname = input("send to: ")
    text = input("message text: ")
    msg.send_message(uname, text)


def read(msg: BlockchainMessage):
    """

    :param msg:
    :return:
    """
    for x in msg.d.messages:
        print("{0}: {1}".format(x.fr.uname, x.text))


def main():
    """

    :return:
    """
    addr = input("addr > ")
    uname = input("uname > ")
    email = input("email > ")
    msg = BlockchainMessage(uname)
    msg.d.add_contact(addr, uname, email)
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
        if cmd == "exit":
            done = True


if __name__ == "__main__":
    main()
