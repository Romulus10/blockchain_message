package io.github.romulus10.blckchnmsg.blckchnmsg

import android.util.Log
import io.github.romulus10.blckchnmsg.BlckChnMsgStorage
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Message
import org.web3j.crypto.WalletUtils
import org.web3j.protocol.Web3jFactory
import org.web3j.protocol.http.HttpService
import org.web3j.tx.Contract.GAS_LIMIT
import org.web3j.tx.ManagedTransaction.GAS_PRICE


class Blockchain {
    fun send(msg: Message.Message) {
        val web3j = Web3jFactory.build(HttpService())
        val credentials = WalletUtils.loadCredentials("password", "/path/to/walletfile")
        Log.d("BLOCKCHAIN", "Connected to Ethereum client version: " + web3j.web3ClientVersion().send().web3ClientVersion)
        val contract = BlckChnMsgStorage.load("0x<address>|<ensName>", web3j, credentials, GAS_PRICE, GAS_LIMIT)
        val msgPacket = (msg.id.toString() + "♣" + msg.to.id.toString() + "♣" + msg.from.toString() + "♣" + msg.message + "♣" + msg.signature)
        contract.store(msg.id.toBigInteger(), msg.to.id.toBigInteger(), msgPacket)
    }

    fun recv(userId: Int, lastMessage: Int): MutableList<Message.Message> {
        val web3j = Web3jFactory.build(HttpService())
        val credentials = WalletUtils.loadCredentials("password", "/path/to/walletfile")
        Log.d("BLOCKCHAIN", "Connected to Ethereum client version: " + web3j.web3ClientVersion().send().web3ClientVersion)
        val contract = BlckChnMsgStorage.load("0x<address>|<ensName>", web3j, credentials, GAS_PRICE, GAS_LIMIT)
        val result = contract.retrieve(userId.toBigInteger(), lastMessage.toBigInteger()).send()
        val resultArray = result.split("♠")
        val messages: MutableList<Message.Message> = mutableListOf()
        for (x in resultArray) {
            val y = x.split('♣')
            var c: Contact.Contact? = null
            if (y.size == 5) {
                for (z in Contact.ITEMS) {
                    if (z.uname == y[2]) {
                        c = z
                    }
                }
            }
            messages.add(Message.createMessage(y[0].toInt(), Contact.ITEMS[0], c, y[3], y[4], false))
        }
        return messages
    }
}