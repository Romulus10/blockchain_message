#!/usr/bin/env python3

from solc import compile_source
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

src = '''
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

compiled = compile_source(src)
contract_interface = compiled['<stdin>:Greeter']

w3 = Web3(HTTPProvider("http://localhost:8545"))


print(w3.eth.getBlock('latest').number)

addr = '0x1243a7cFCb0818A99f72bE0cbC0824702A0c2745'

print("Address: {}".format(addr))

abi = contract_interface['abi']
contract = w3.eth.contract(address=addr, abi=abi, ContractFactoryClass=ConciseContract)

print('Contract value: {}'.format(contract.greet()))
contract.setGreeting('Hello, World!', transact={'from': w3.eth.accounts[0]})
print('Setting value.')
print('Contract value: {}'.format(contract.greet()))
