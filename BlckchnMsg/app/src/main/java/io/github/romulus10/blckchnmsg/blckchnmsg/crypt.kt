package io.github.romulus10.blckchnmsg.blckchnmsg

import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact
import java.security.KeyPairGenerator
import java.security.PrivateKey
import java.security.PublicKey
import javax.crypto.Cipher

class Crypt {
    constructor(publicKey: PublicKey?, privateKey: PrivateKey?) {

        this.publicKey = publicKey
        this.privateKey = privateKey
    }

    private var publicKey: PublicKey?

    private var privateKey: PrivateKey?

    fun generate_key(uname: String) {
        val kpg = KeyPairGenerator.getInstance("RSA")
        kpg.initialize(1024)
        val kp = kpg.genKeyPair()
        this.publicKey = kp.public
        this.privateKey = kp.private
    }

    fun import_key(addr: String, filename: String, email: String): Contact? {
        return null
    }

    fun encrypt(message: String, recipient: Contact): ByteArray {
        val cipher = Cipher.getInstance("RSA")
        cipher.init(Cipher.ENCRYPT_MODE, publicKey)
        return cipher.doFinal(message.toByteArray())
    }

    fun decrypt(message: ByteArray): String {
        val cipher=Cipher.getInstance("RSA")
        cipher.init(Cipher.DECRYPT_MODE, privateKey)
        val decryptedBytes = cipher.doFinal(message)
        return String(decryptedBytes)
    }

    fun sign(message: String): String {
        return ""
    }

    fun verify(message: String, signature: String, sender: Contact): Boolean {
        return false
    }
}