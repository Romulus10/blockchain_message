package io.github.romulus10.blckchnmsg.blckchnmsg

import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact

class Crypt {
    constructor() {

    }

    fun generate_key(uname: String) {

    }

    fun import_key(addr: String, filename: String, email: String): Contact? {
        return null
    }

    fun encrypt(message: String, recipient: Contact): ByteArray {
        return ByteArray(0)
    }

    fun decrypt(message: ByteArray): String {
        return ""
    }

    fun sign(message: String): String {
        return ""
    }

    fun verify(message: String, signature: String, sender: Contact): Boolean {
        return false
    }
}