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

pub struct BlockchainMessage {
    max: i32,
    id: Contact
}

// TODO BlockchainMessage implementation.

pub fn send(i: BlockchainMessage, msg: String, to: Vec<Contact>) -> i32 {
    i.max = i.max + 1;
    let c = Crypt::new(String::from(i.id.email));
    let msg_se = c.sign(c.encrypt(msg));
    let message = Message {
        id: i.max,
        from: i.id,
        message: msg_se
    };
}

pub fn recv(i: BlockchainMessage) -> Message {
    Message {
        id: 0,
        from: 0, // TODO This is a filler.
        message: "String." // TODO This is a filler.
    }
}
