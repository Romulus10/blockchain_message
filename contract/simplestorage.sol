pragma solidity ^0.4.0;
import "./Storage.sol";

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
}
