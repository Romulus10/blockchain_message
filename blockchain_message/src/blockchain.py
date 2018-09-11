from typing import List

from solc import compile_files
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

from blockchain_message.src.core import Message, Contact


# noinspection PyUnresolvedReferences
class Blockchain(object):
    """
    """

    def __init__(self):
        """
        """
        with open('./.blkchnmsg/contract', 'r') as f:
            self.addr = f.read()
        compiled = compile_files(['./../contract/contracts/blockchain_message.sol'])
        self.contract_interface = compiled['./../contract/contracts/blockchain_message.sol:BlckChnMsgStorage']
        self.w3 = Web3(HTTPProvider("http://localhost:7545"))
        self.contract = self.w3.eth.contract(abi=self.contract_interface['abi'],
                                             bytecode=self.contract_interface['bin'])

    def submit(self, message: Message):
        """
        :param message:
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi, ContractFactoryClass=ConciseContract)

        msg_id = message.id
        to_user = message.to.uname
        fr_user = message.fr.uname
        msg_text = message.text
        sign = message.sign
        message_body = ('{0}♣{1}♣{2}♣{3}♣{4}'.format(msg_id, to_user, fr_user, msg_text, sign)).encode('utf8')

        to_user = int(message.to.address)
        contract.store(msg_id, to_user, message_body, transact={'from': self.w3.eth.accounts[0]})

    def retrieve(self, user: Contact, last_message: int, contact_list: List[Contact]) -> List[Message]:
        """
        :return:
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi)

        result = contract.functions.retrieve(int(user.address), last_message).call()

        result = bytes(result, 'utf8')
        result = result.decode('utf8')

        messages = list()

        res_list = result.split('♠')
        for x in res_list:
            y = x.split('♣')
            c: Contact = None
            if len(y) == 5:
                for z in contact_list:
                    if z.uname == y[2]:
                        c = z
                if c is None:
                    c = Contact('', y[2], '')
                messages.append(Message(int(y[0]), user, c, y[3], y[4], False))
        return messages
