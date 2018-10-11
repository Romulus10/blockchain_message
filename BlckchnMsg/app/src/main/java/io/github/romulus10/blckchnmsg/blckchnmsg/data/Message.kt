package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.ArrayList
import java.util.HashMap

object Message {

    val ITEMS: MutableList<Message> = ArrayList()

    val ITEM_MAP: MutableMap<String, Message> = HashMap()

    fun addItem(item: Message) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
    }

    fun createMessage(id: String, to: Contact.Contact, from: Contact.Contact?, message: String, signature: String): Message {
        return Message(id, to, from, message, signature, false)
    }

    data class Message(val id: String, val to: Contact.Contact, val from: Contact.Contact?, val message: String, val signature: String, val verified: Boolean) {
        override fun toString(): String = message
    }
}
