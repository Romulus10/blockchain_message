package io.github.romulus10.blckchnmsg.blckchnmsg

import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Message

class Database {
    constructor() {

    }

    fun add_contact(addr: String, uname: String, email: String): Boolean {
        return false
    }

    fun read_contact(uname: String): Contact? {
        return null
    }

    fun del_contact(uname: String): Boolean {
        return false
    }

    fun insert(to: Contact, fr: Contact, text: String, sign: String, verified: Boolean): Message? {
        return null
    }

    fun delete(msgid: Int): Boolean {
        return false
    }

    fun message_index(): Int {
        return 0
    }
}