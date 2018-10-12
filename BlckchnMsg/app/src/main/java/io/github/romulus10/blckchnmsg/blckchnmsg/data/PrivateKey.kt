package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.*

object PrivateKey {

    val ITEMS: MutableList<PrivateKey> = ArrayList()

    val ITEM_MAP: MutableMap<String, PrivateKey> = HashMap()

    fun addItem(item: PrivateKey) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
    }

    fun createKey(id: String, user: Contact.Contact, key: java.security.PrivateKey): PrivateKey {
        return PrivateKey(id, user, key)
    }

    data class PrivateKey(val id: String, val user: Contact.Contact, val key: java.security.PrivateKey) {
        override fun toString(): String = id
    }
}
