package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.ArrayList
import java.util.HashMap

object Contact {

    val ITEMS: MutableList<Contact> = ArrayList()

    val ITEM_MAP: MutableMap<String, Contact> = HashMap()

    private val COUNT = 25

    private fun addItem(item: Contact) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
    }

    private fun createContact(id: String, uname: String, email: String, key: String): Contact {
        return Contact(id, uname, email, key)
    }

    data class Contact(val id: String, val uname: String, val email: String, val key: String) {
        override fun toString(): String = uname
    }
}
