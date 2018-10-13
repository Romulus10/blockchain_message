package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.security.PublicKey
import java.util.*

object Contact {

    val ITEMS: MutableList<Contact> = ArrayList()

    val ITEM_MAP: MutableMap<Int, Contact> = HashMap()

    fun getContact(id: Int): Contact? {
        return ITEM_MAP[id]
    }

    fun addItem(item: Contact) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
    }

    fun createContact(id: Int, uname: String, email: String): Contact {
        return Contact(id, uname, email, null)
    }

    data class Contact(val id: Int, val uname: String, val email: String, val publicKey: PublicKey?) {
        override fun toString(): String = uname
    }
}
