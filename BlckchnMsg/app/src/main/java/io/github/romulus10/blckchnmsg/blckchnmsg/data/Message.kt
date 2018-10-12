package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.*

object Message {

    val ITEMS: MutableList<Message> = ArrayList()

    val ITEM_MAP: MutableMap<Int, Message> = HashMap()

    var TOP_MESSAGE_ID: Int = 0

    fun addItem(item: Message) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
        TOP_MESSAGE_ID = item.id
    }

    fun lastMessage(): Int {
        return TOP_MESSAGE_ID
    }

    fun createMessage(id: Int, to: Contact.Contact, from: Contact.Contact?, message: String, signature: String, verified: Boolean): Message {
        return Message(id, to, from, message, signature, verified)
    }

    data class Message(val id: Int, val to: Contact.Contact, val from: Contact.Contact?, val message: String, val signature: String, val verified: Boolean) {
        override fun toString(): String = message
    }
}
