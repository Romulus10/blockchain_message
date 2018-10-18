#!/usr/bin/env python3

from solc import compile_files
from web3 import Web3, HTTPProvider

compiled_storage = compile_files(["./contract/contracts/blockchain_message.sol"])
compiled_manager = compile_files(["./contract/contracts/identity_manager.sol"])
storage_interface = compiled_storage['./contract/contracts/blockchain_message.sol:BlckChnMsgStorage']
manager_interface = compiled_manager['./contract/contracts/identity_manager.sol:IdentityManager']

w3 = Web3(HTTPProvider("http://localhost:7545"))

print(w3.eth.getBlock('latest').number)
storage_contract = w3.eth.contract(abi=storage_interface['abi'], bytecode=storage_interface['bin'])
manager_contract = w3.eth.contract(abi=manager_interface['abi'], bytecode=manager_interface['bin'])

tx_a = storage_contract.constructor().transact(transaction={'from': w3.eth.accounts[0], 'gas': 5000000})
tx_b = manager_contract.constructor().transact(transaction={'from': w3.eth.accounts[0], 'gas': 5000000})

receipt_a = w3.eth.getTransactionReceipt(tx_a)
receipt_b = w3.eth.getTransactionReceipt(tx_b)

addr_a = receipt_a['contractAddress']
addr_b = receipt_b['contractAddress']

print("Address: {}".format(addr_a))
print("Address: {}".format(addr_b))

with open('./client/.blkchnmsg/contract', 'w') as f:
    f.write(addr_a + "\n")
    f.write(addr_b)
