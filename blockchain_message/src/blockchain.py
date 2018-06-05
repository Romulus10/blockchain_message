from solc import compile_files
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

from blockchain_message.src.core import Message


# noinspection PyUnresolvedReferences
class Blockchain(object):
    """
    """

    def __init__(self):
        """
        """
        # TODO Read contract address somehow? Probably config file.
        self.addr = ''
        compiled = compile_files('./contract/storage.sol')
        self.contract_interface = compiled('<stdin>:BlckChnMsgStorage')
        self.w3 = Web3(HTTPProvider("http://localhost:8545"))
        self.contract = self.w3.eth.contract(abi=self.contract_interface['abi'],
                                             bytecode=self.contract_interface['bin'])

    def submit(self, message: Message) -> bool:
        """
        :param message:
        :return: Did our message send correctly?
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi, ContractFactoryClass=ConciseContract)

        msg_id = message.id.encode('utf8')
        to_user = message.to.uname.encode('utf8')
        fr_user = message.fr.uname.encode('utf8')
        msg_text = message.text.encode('utf8')
        message_body = '{0},{1},{2},{3}'.format(msg_id, to_user, fr_user, msg_text)

        tx = contract.store(msg_id, to_user, message_body, transact={'from': self.w3.eth.accounts[0]})
        receipt = w3.eth.getTransactionReceipt(tx)
        addr = receipt['contractAddress']

        if addr:
            return True
        else:
            return False

    def retrieve(self, username, key) -> List[Message]:
        """
        :return:
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi, ContractFactoryClass=ConciseContract)

        # TODO Figure out how to tell what message ids we need to download.
        # TODO We could probably get a list of all relevant messages from the contract...
        # TODO That's going to get absurdly expensive.
        result = contract.retrieve(username, key, transact={'from': self.w3.eth.accounts[0]})

        messages = list()

        res_list = result.split(';')
        for x in res_list:
            y = x.split(',')
            messages.append(Message(y[0], y[1], y[2], y[3]))

        return messages
