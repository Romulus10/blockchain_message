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
        # Read contract address somehow?
        self.addr = ''
        compiled = compile_files('./proof/contract/storage.sol')
        self.contract_interface = compiled('<stdin>:BlckChnMsgStorage')
        self.w3 = Web3(HTTPProvider("http://localhost:8545"))
        self.contract = self.w3.eth.contract(abi=self.contract_interface['abi'],
                                             bytecode=self.contract_interface['bin'])

    def submit(self, message: Message) -> int:
        """
        :param message:
        :return:
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi, ContractFactoryClass=ConciseContract)

        addr = self.w3.toBytes(hexstr='0x12345')
        key = self.w3.toBytes(hexstr='0x0')
        contract.store(addr, key, 'Works.', transact={'from': self.w3.eth.accounts[0]})

    def retrieve(self) -> Message:
        """
        :return:
        """
        abi = self.contract_interface['abi']
        contract = self.w3.eth.contract(address=self.addr, abi=abi, ContractFactoryClass=ConciseContract)

        addr = self.w3.toBytes(hexstr='0x12345')
        key = self.w3.toBytes(hexstr='0x0')
        contract.store(addr, key, 'Works.', transact={'from': self.w3.eth.accounts[0]})
