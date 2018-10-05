package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.ArrayList
import java.util.HashMap

object Key {

    val ITEMS: MutableList<Key> = ArrayList()

    val ITEM_MAP: MutableMap<String, Key> = HashMap()

    private val COUNT = 25


    private fun addItem(item: Key) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
    }

    private fun createKey(id: String, user: Contact.Contact, key: String): Key {
        return Key(id, user, key)
    }

    data class Key(val id: String, val user: Contact.Contact, val key: String) {
        override fun toString(): String = id
    }
}
