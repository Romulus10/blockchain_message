pragma solidity ^0.4.7;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/IdentityManager.sol";

contract TestIdentity {
  function test_initial_identity() public {
    IdentityManager id = IdentityManager(DeployedAddresses.IdentityManager());

    uint expected = 0;

    Assert.equal(id.get_my_identity("test", "test"), expected, "Owner should have 10000 MetaCoin initially");
  }
}
