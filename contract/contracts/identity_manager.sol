pragma solidity ^0.4.7;

contract IdentityManager {
    string[10] users;
    uint latest;

    function new_identity(string uname) public returns (uint) {
        users[latest] = uname;
        latest++;
    }

    function get_identity(string uname) public view returns (uint) {
         uint result = 11;

         for (uint i = 0; i < 10; i++) {
            if (stringsEqual(users[i], uname)) {
                result = i;
            }
         }

         if (result == 11) {
            result = new_identity(uname);
         }

         return result;
    }

    function stringsEqual(string storage _a, string memory _b) internal view returns (bool) {
		bytes storage a = bytes(_a);
		bytes memory b = bytes(_b);
		if (a.length != b.length)
			return false;
		for (uint i = 0; i < a.length; i ++)
			if (a[i] != b[i])
				return false;
		return true;
	}
}
