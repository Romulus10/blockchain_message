package io.github.romulus10.blckchnmsg.blckchnmsg

import android.os.Environment
import io.github.romulus10.blckchnmsg.blckchnmsg.Imports.import_priv_key
import io.github.romulus10.blckchnmsg.blckchnmsg.Imports.import_pub_key
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.security.KeyPairGenerator
import java.security.PrivateKey
import java.security.PublicKey
import javax.crypto.Cipher

class Crypt {

    internal var publicKey: PublicKey? = null

    private var privateKey: PrivateKey? = null

    private fun write_private_file() {
        val path = Environment.getExternalStorageDirectory()
        val directory = File(path, "blckchnmsg/.keys")
        directory.mkdirs()
        val file = File(directory, Contact.ITEMS[0].uname+".priv")
        FileOutputStream(file).use {
            it.write(privateKey.toString().toByteArray())
        }
    }

    private fun write_public_file() {
        val path = Environment.getExternalStorageDirectory()
        val directory = File(path, "blckchnmsg/.keys")
        directory.mkdirs()
        val file = File(directory, Contact.ITEMS[0].uname+".pub")
        FileOutputStream(file).use {
            it.write(privateKey.toString().toByteArray())
        }
    }

    private fun read_private_file(): String {
        val path = Environment.getExternalStorageDirectory()
        val directory = File(path, "blckchnmsg/.keys")
        directory.mkdirs()
        val file = File(directory, Contact.ITEMS[0].uname+".priv")
        return FileInputStream(file).bufferedReader().use {
            it.readText()
        }
    }

    private fun read_public_file(uname: String): String {
        val path = Environment.getExternalStorageDirectory()
        val directory = File(path, "blckchnmsg/.keys")
        directory.mkdirs()
        val file = File(directory, "$uname.pub")
        return FileInputStream(file).bufferedReader().use {
            it.readText()
        }
    }

    fun generate_key(uname: String) {
        val kpg = KeyPairGenerator.getInstance("RSA")
        kpg.initialize(1024)
        val kp = kpg.genKeyPair()
        this.publicKey = kp.public
        this.privateKey = kp.private
    }

    fun encrypt(message: String, recipient: Contact.Contact?): ByteArray {
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

    fun setKeys() {
        this.publicKey = import_pub_key(Contact.ITEMS[0].uname)
        this.privateKey = import_priv_key(Contact.ITEMS[0].uname)
    }
}

object Imports {
    fun import_pub_key(filename: String): PublicKey? {
        return null
    }

    fun import_priv_key(filename: String): PrivateKey? {
        return null
    }
}