use ethabi;
use web3::types::Address;

pub struct KeyVal {
    /// # pub struct KeyVal
    pub key: String,
    pub val: String
}

pub struct Blockchain {
    /// # pub struct BlockChain
    pub memory: Vec<KeyVal>,
    cAddr: Address,
    ethabi: ethabi::Contract
}
