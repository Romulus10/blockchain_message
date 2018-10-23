const idmgr = artifacts.require("./IdentityManager.sol")
const blchn = artifacts.require("./BlckChnMsgStorage.sol")

module.exports = function(deployer) {
  deployer.deploy(idmgr);
  deployer.deploy(blchn);
}
