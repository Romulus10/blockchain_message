pragma solidity ^0.4.7;

contract BlckChnMsgStorage {
    string[100][100] db;
    uint256 length;

    function store(uint to_user, string val) public {
        db[to_user][length] = val;
        length++;
    }

    function retrieve(uint to_user, uint key) public view returns (string) {
        string memory messages;
        uint256 max = length;
        for (uint i = key; i < max; i++) {
            messages = strConcat(messages, db[to_user][i], "♠");
        }
        return messages;
    }

    function strConcat(string _a, string _b, string _c) internal pure returns (string){
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
