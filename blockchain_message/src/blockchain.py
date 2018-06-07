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
        compiled = compile_files(['./../../contract/blockchain_message.sol'])
        self.contract_interface = compiled['./../../contract/blockchain_message.sol:BlckChnMsgStorage']
        self.w3 = Web3(HTTPProvider("http://localhost:7545"))
        self.contract = self.w3.eth.contract(abi=self.contract_interface['abi'],
                                             bytecode=self.contract_interface['bin'])

    def submit(self, message: Message) -> bool:
        """
        :param message:
        :return: Did our message send correctly?
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi, ContractFactoryClass=ConciseContract)

        msg_id = message.id
        to_user = message.to.uname.encode('utf8')
        fr_user = message.fr.uname.encode('utf8')
        msg_text = message.text.encode('utf8')
        message_body = '{0},{1},{2},{3}'.format(msg_id, to_user, fr_user, msg_text)

        to_user = int(message.to.address)
        tx = contract.store(msg_id, to_user, message_body, transact={'from': self.w3.eth.accounts[0]})
        receipt = self.w3.eth.getTransactionReceipt(tx)
        addr = receipt['contractAddress']

        if addr:
            return True
        else:
            return False

    def retrieve(self, user: Contact, last_message: int) -> List[Message]:
        """
        :return:
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi, ContractFactoryClass=ConciseContract)

        result = contract.retrieve(int(user.address), last_message, transact={'from': self.w3.eth.accounts[0]})

        messages = list()

        res_list = result.split(';')
        for x in res_list:
            y = x.split(',')
            messages.append(Message(y[0], y[1], y[2], y[3]))

        return messages
