package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.ArrayList
import java.util.HashMap

/**
 * Helper class for providing sample content for user interfaces created by
 * Android template wizards.
 *
 * TODO: Replace all uses of this class before publishing your app.
 */
object Contact {

    /**
     * An array of sample (dummy) items.
     */
    val ITEMS: MutableList<Contact> = ArrayList()

    /**
     * A map of sample (dummy) items, by ID.
     */
    val ITEM_MAP: MutableMap<String, Contact> = HashMap()

    private val COUNT = 25

    init {
        // Add some sample items.
        for (i in 1..COUNT) {
            addItem(createContact(i))
        }
    }

    private fun addItem(item: Contact) {
        ITEMS.add(item)
        ITEM_MAP.put(item.id, item)
    }

    private fun createContact(position: Int): Contact {
        return Contact(position.toString(), "Item $position", makeDetails(position))
    }

    private fun makeDetails(position: Int): String {
        val builder = StringBuilder()
        builder.append("Details about Item: ").append(position)
        for (i in 0 until (position - 1)) {
            builder.append("\nMore details information here.")
        }
        return builder.toString()
    }

    data class Contact(val id: String, val content: String, val details: String) {
        override fun toString(): String = content
    }
}
