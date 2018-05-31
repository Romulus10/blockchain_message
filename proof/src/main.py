#!/usr/bin/env python3

import json
import web3

from web3 import Web3, HTTPProvider
from solc import compile_source
from web3.contract import ConciseContract

src = '''
pragma solidity ^0.4.0;

contract Storage {
  mapping (bytes32 => string) public storg;

  function store(bytes32 key, string val) public {
    storg[key] = val;
  }

  function get(bytes32 key) public returns (string) {
    return storg[key];
  }
}

contract YadqlStorage {
  mapping (bytes16 => Storage) public db;

  function store(bytes16 pubkey, bytes32 key, string val) public {
    if (db[pubkey] != address(0x0)) {
      db[pubkey].store(key, val);
    } else {
      Storage x = new Storage();
      db[pubkey] = x;
      x.store(key, val);
    }
  }

  function retrieve(bytes16 pubkey, bytes32 key) public returns (string) {
    return db[pubkey].get(key);
  }
}
'''

compiled = compile_source(src)
contract_interface = compiled['<stdin>:YadqlStorage']

w3 = Web3(HTTPProvider("http://localhost:8545"))


print(w3.eth.getBlock('latest').number)
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

tx = contract.constructor().transact(transaction={'from': w3.eth.accounts[0], 'gas': 5000000})

receipt = w3.eth.getTransactionReceipt(tx)
addr = receipt['contractAddress']

print("Address: {}".format(addr))

abi = contract_interface['abi']
contract = w3.eth.contract(address=addr, abi=abi, ContractFactoryClass=ConciseContract)

addr = w3.toBytes(hexstr='0x12345')
key = w3.toBytes(hexstr='0x0')
contract.store(addr, key, 'Works.', transact={'from': w3.eth.accounts[0]})

print('Contract value: {}'.format(contract.retrieve(12345, 0)))
