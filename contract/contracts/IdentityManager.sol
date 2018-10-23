pragma solidity ^0.4.7;

contract IdentityManager {
    string[3][100] users;
    uint latest;

    function get_identity(string uname) public view returns (uint) {
         uint result = 999;

         for (uint i = 0; i < 100; i++) {
            if (stringsEqual(users[i][0], uname)) {
                    result = i;
            }
         }

         return result;
    }

    function new_identity(string uname, string password) internal returns (uint) {

        if (latest >= 100) return 9999;

        users[latest][0] = uname;
        users[latest][2] = password;
        return latest++;
    }

    function get_my_identity(string uname, string password) public returns (uint) {
         uint result = 999;

         for (uint i = 0; i < 100; i++) {
            if (stringsEqual(users[i][0], uname)) {
                if (stringsEqual(users[i][2], password)) {
                    result = i;
                } else {
                    result = 99999;
                }
            }
         }

         if (result == 999) {
            result = new_identity(uname, password);
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
