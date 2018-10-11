package io.github.romulus10.blckchnmsg

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView


import io.github.romulus10.blckchnmsg.MessageFragment.OnListFragmentInteractionListener
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Message

import kotlinx.android.synthetic.main.fragment_message.view.*

class MyMessageRecyclerViewAdapter(
        private val mValues: MutableList<Message.Message>,
        private val mListener: OnListFragmentInteractionListener?)
    : RecyclerView.Adapter<MyMessageRecyclerViewAdapter.ViewHolder>() {

    private val mOnClickListener: View.OnClickListener

    init {
        mOnClickListener = View.OnClickListener { v ->
            val item = v.tag as Message.Message
            mListener?.onListFragmentInteraction(item)
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.fragment_message, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val item = mValues[position]
        holder.mIdView.text = item.from?.uname
        holder.mContentView.text = item.message

        with(holder.mView) {
            tag = item
            setOnClickListener(mOnClickListener)
        }
    }

    override fun getItemCount(): Int = mValues.size

    inner class ViewHolder(val mView: View) : RecyclerView.ViewHolder(mView) {
        val mIdView: TextView = mView.item_number
        val mContentView: TextView = mView.content

        override fun toString(): String {
            return super.toString() + " '" + mContentView.text + "'"
        }
    }
}
