package io.github.romulus10.blckchnmsg

import android.content.Context
import android.net.Uri
import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact
import kotlinx.android.synthetic.main.fragment_new_contact.*

class NewContact : Fragment(), View.OnClickListener {
    private var listener: OnFragmentInteractionListener? = null

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        create_contact.setOnClickListener(this)
        return inflater.inflate(R.layout.fragment_new_contact, container, false)
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

    override fun onClick(v: View) {
        Contact.addItem(Contact.createContact(
                addr.text.toString().toInt(),
                uname.text.toString(),
                email.text.toString()))
    }

    interface OnFragmentInteractionListener {
        fun onFragmentInteraction(uri: Uri)
    }

    companion object {
        @JvmStatic
        fun newInstance(param1: String, param2: String) =
                NewContact().apply {
                    arguments = Bundle().apply {
                    }
                }
    }
}
