package io.github.romulus10.blckchnmsg

import android.content.Context
import android.net.Uri
import android.os.Bundle
import android.support.v4.app.Fragment
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import io.github.romulus10.blckchnmsg.blckchnmsg.Crypt
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Message
import kotlinx.android.synthetic.main.fragment_new_message.*


class NewMessage : Fragment(), View.OnClickListener {

    private var contact: Int = 0
    private var crypt: Crypt = Crypt()

    override fun onClick(v: View?) {
        Message.addItem(Message.createMessage(
                (Message.TOP_MESSAGE_ID + 1),
                Contact.ITEMS[0],
                Contact.getContact(contact),
                crypt.encrypt(message_text.text.toString(), Contact.getContact(contact)).toString(),
                crypt.sign(message_text.text.toString()),
                true))
    }

    private var listener: OnFragmentInteractionListener? = null

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        message_send.setOnClickListener(this)

        val spinnerArrayAdapter = ArrayAdapter<Contact.Contact>(
                activity!!.applicationContext,
                contact_spinner.id,
                Contact.ITEMS
        )

        spinnerArrayAdapter.setDropDownViewResource(contact_spinner.id)
        contact_spinner?.adapter = spinnerArrayAdapter

        contact_spinner?.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parentView: AdapterView<*>, selectedItemView: View, position: Int, id: Long) {
                Log.d("SPINNER", position.toString())
                contact = (parentView.getItemAtPosition(position) as Contact.Contact).id
            }

            override fun onNothingSelected(parentView: AdapterView<*>) {
                // your code here
            }
        }

        return inflater.inflate(R.layout.fragment_new_message, container, false)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is OnFragmentInteractionListener) {
            listener = context
        } else {
            throw RuntimeException(context.toString() + " must implement OnFragmentInteractionListener")
        }
    }

    override fun onDetach() {
        super.onDetach()
        listener = null
    }

    interface OnFragmentInteractionListener {
        fun onFragmentInteraction(uri: Uri)
    }
}
