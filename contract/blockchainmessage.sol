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
    value = db[pubkey].get(key);
  }
}
