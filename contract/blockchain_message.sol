pragma solidity ^0.4.0;

contract Storage {
    mapping(uint => string) public storg;
    uint public length = 0;

    function store(uint key, string val) public {
        storg[key] = val;
        length++;
    }

    function get(uint key) public returns (string) {
        return storg[key];
    }
}

contract BlckChnMsgStorage {
    mapping(uint => Storage) public db;

    function store(uint key, uint to_user, string val) public {
        if (db[to_user] != address(0x0)) {
            db[to_user].store(key, val);
        } else {
            Storage x = new Storage();
            db[to_user] = x;
            x.store(key, val);
        }
    }

    function retrieve(uint to_user, uint key) public returns (string) {
        string memory messages;
        for (uint i = key; i < db[to_user].length(); i++) {
            messages = strConcat(messages, db[to_user].get(i), "♠");
        }
        return messages;
        return db[to_user].get(key);
    }

    function strConcat(string _a, string _b, string _c) internal returns (string){
        bytes memory _ba = bytes(_a);
        bytes memory _bb = bytes(_b);
        bytes memory _bc = bytes(_c);
        string memory abc = new string(_ba.length + _bb.length + _bc.length);
        bytes memory babcde = bytes(abc);
        uint k = 0;
        for (uint i = 0; i < _ba.length; i++) babcde[k++] = _ba[i];
        for (i = 0; i < _bb.length; i++) babcde[k++] = _bb[i];
        for (i = 0; i < _bc.length; i++) babcde[k++] = _bc[i];
        return string(babcde);
    }
}
