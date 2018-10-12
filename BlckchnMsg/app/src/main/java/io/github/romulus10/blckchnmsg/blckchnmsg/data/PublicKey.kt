package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.*

object PublicKey {

    val ITEMS: MutableList<PublicKey> = ArrayList()

    val ITEM_MAP: MutableMap<String, PublicKey> = HashMap()

    fun addItem(item: PublicKey) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
    }

    fun createKey(id: String, user: Contact.Contact, key: java.security.PublicKey): PublicKey {
        return PublicKey(id, user, key)
    }

    data class PublicKey(val id: String, val user: Contact.Contact, val key: java.security.PublicKey) {
        override fun toString(): String = id
    }
}
