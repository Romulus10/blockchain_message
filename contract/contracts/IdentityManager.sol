pragma solidity ^0.4.7;

contract IdentityManager {
    string[100] users;
    uint latest;

    function get_identity(string uname) public view returns (uint) {
         uint result = 999;

         for (uint i = 0; i < 100; i++) {
            if (stringsEqual(users[i], uname)) {
                    result = i;
            }
         }

         return result;
    }

    function new_identity(string uname) public returns (uint) {

        if (latest >= 100) return 9999;

        uint ret_val = latest++;
        users[latest] = uname;
        return ret_val;
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
