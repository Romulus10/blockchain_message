package io.github.romulus10.blckchnmsg.blckchnmsg.data

import java.util.ArrayList
import java.util.HashMap

/**
 * Helper class for providing sample content for user interfaces created by
 * Android template wizards.
 *
 * TODO: Replace all uses of this class before publishing your app.
 */
object Message {

    /**
     * An array of sample (dummy) items.
     */
    val ITEMS: MutableList<Message> = ArrayList()

    /**
     * A map of sample (dummy) items, by ID.
     */
    val ITEM_MAP: MutableMap<String, Message> = HashMap()

    private val COUNT = 25

    init {
        // Add some sample items.
        for (i in 1..COUNT) {
            addItem(createMessage(i))
        }
    }

    private fun addItem(item: Message) {
        ITEMS.add(item)
        ITEM_MAP[item.id] = item
    }

    private fun createMessage(position: Int): Message {
        return Message(position.toString(), "Item $position", makeDetails(position))
    }

    private fun makeDetails(position: Int): String {
        val builder = StringBuilder()
        builder.append("Details about Item: ").append(position)
        for (i in 0 until (position - 1)) {
            builder.append("\nMore details information here.")
        }
        return builder.toString()
    }

    /**
     * A dummy item representing a piece of content.
     */
    data class Message(val id: String, val content: String, val details: String) {
        override fun toString(): String = content
    }
}
