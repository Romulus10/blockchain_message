extern crate gpgme;
extern crate regex;
extern crate web3;
extern crate ethabi;

mod blockchain;
mod crypt;
mod database;
mod core;

use database::database::Database;
use blockchain::blockchain::Blockchain;
use crypt::crypt::Crypt;
use core::core::Message;
use core::core::Contact;

struct BlockchainMessage {
    database: Database,
    crypt: Crypt,
    blockchain: Blockchain
}

pub fn send(msg: String, to: Vec<Contact>) -> i32 {
    0
}

pub fn recv() -> Message {
    Message {
        id: 0,
        from: 0, // TODO This is a filler.
        message: "String." // TODO This is a filler.
    }
}
