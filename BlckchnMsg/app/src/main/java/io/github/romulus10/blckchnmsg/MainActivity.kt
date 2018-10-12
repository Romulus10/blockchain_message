package io.github.romulus10.blckchnmsg

import android.net.Uri
import android.os.Bundle
import android.support.design.widget.NavigationView
import android.support.v4.view.GravityCompat
import android.support.v7.app.ActionBarDrawerToggle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Contact
import io.github.romulus10.blckchnmsg.blckchnmsg.data.Message
import io.github.romulus10.blckchnmsg.blckchnmsg.data.PublicKey
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.app_bar_main.*

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener,
        MessageFragment.OnListFragmentInteractionListener,
        ContactFragment.OnListFragmentInteractionListener,
        ListKeysFragment.OnListFragmentInteractionListener,
        NewContact.OnFragmentInteractionListener,
        NewMessage.OnFragmentInteractionListener,
        KeysFragment.OnFragmentInteractionListener {
    override fun onListFragmentInteraction(item: PublicKey.PublicKey) {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun onFragmentInteraction(uri: Uri) {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun onListFragmentInteraction(item: Message.Message) {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun onListFragmentInteraction(item: Contact.Contact) {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        val toggle = ActionBarDrawerToggle(
                this, drawer_layout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close)
        drawer_layout.addDrawerListener(toggle)
        toggle.syncState()

        nav_view.setNavigationItemSelectedListener(this)


        Log.d("MainActivity", "Messages")
        val fragmentManager = supportFragmentManager
        val fragmentTransaction = fragmentManager.beginTransaction()
        val fragment = MessageFragment()
        val b = Bundle()
        fragment.arguments = b
        fragmentTransaction.replace(R.id.fragment_container, fragment)
                .addToBackStack("Messages").commit()
        title = "Messages"
    }

    override fun onBackPressed() {
        if (drawer_layout.isDrawerOpen(GravityCompat.START)) {
            drawer_layout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_settings -> true
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        // Handle navigation view item clicks here.
        when (item.itemId) {
            R.id.nav_messages -> {
                Log.d("MainActivity", "Messages")
                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()
                val fragment = MessageFragment()
                val b = Bundle()
                fragment.arguments = b
                fragmentTransaction.replace(R.id.fragment_container, fragment)
                        .addToBackStack("Messages").commit()
                title = "Messages"
            }
            R.id.nav_contacts -> {
                Log.d("MainActivity", "Contacts")
                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()
                val fragment = ContactFragment()
                val b = Bundle()
                fragment.arguments = b
                fragmentTransaction.replace(R.id.fragment_container, fragment)
                        .addToBackStack("Contacts").commit()
                title = "Contacts"
            }
            R.id.nav_keys -> {
                Log.d("MainActivity", "Keys")
                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()
                val fragment = ListKeysFragment()
                val b = Bundle()
                fragment.arguments = b
                fragmentTransaction.replace(R.id.fragment_container, fragment)
                        .addToBackStack("Keys").commit()
                title = "Keys"
            }
            R.id.nav_new_message -> {
                Log.d("MainActivity", "New Message")
                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()
                val fragment = NewMessage()
                val b = Bundle()
                fragment.arguments = b
                fragmentTransaction.replace(R.id.fragment_container, fragment)
                        .addToBackStack("New Message").commit()
                title = "New Message"
            }

            R.id.nav_new_contact -> {
                Log.d("MainActivity", "New Contact")
                val fragmentManager = supportFragmentManager
                val fragmentTransaction = fragmentManager.beginTransaction()
                val fragment = NewContact()
                val b = Bundle()
                fragment.arguments = b
                fragmentTransaction.replace(R.id.fragment_container, fragment)
                        .addToBackStack("New Contact").commit()
                title = "New Contact"
            }
        }

        drawer_layout.closeDrawer(GravityCompat.START)
        return true
    }
}
