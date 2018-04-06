#!/usr/bin/env python3

import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

contract_source_code = '''
pragma solidity ^0.4.0;

contract Greeter {
    string public greeting;

    function Greeter() {
        greeting = '';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() constant returns (string) {
        return greeting;
    }
}
'''

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:Greeter']

w3 = Web3(HTTPProvider("http://localhost:8545"))

contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

tx_hash = contract.constructor().transact(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

print("Address: {}".format(contract_address))

abi = contract_interface['abi']
contract_instance = w3.eth.contract(address=contract_address, abi=abi,ContractFactoryClass=ConciseContract)

print('Contract value: {}'.format(contract_instance.greet()))
contract_instance.setGreeting('Hello, World!', transact={'from': w3.eth.accounts[0]})
print('Setting value.')
print('Contract value: {}'.format(contract_instance.greet()))

