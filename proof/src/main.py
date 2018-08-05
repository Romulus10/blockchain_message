#!/usr/bin/env python3

from solc import compile_files
from web3 import Web3, HTTPProvider

compiled = compile_files(["./contract/contracts/blockchain_message.sol"])
contract_interface = compiled['./contract/contracts/blockchain_message.sol:BlckChnMsgStorage']

w3 = Web3(HTTPProvider("http://localhost:7545"))


print(w3.eth.getBlock('latest').number)
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

tx = contract.constructor().transact(transaction={'from': w3.eth.accounts[0], 'gas': 5000000})

receipt = w3.eth.getTransactionReceipt(tx)
addr = receipt['contractAddress']

print("Address: {}".format(addr))

with open('./client/.blkchnmsg/contract', 'w') as f:
    f.write(addr)
