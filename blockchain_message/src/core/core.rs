struct Message {
    id: i32,
    to: Vec<Contact>,
    from: Contact,
    text: String
}

struct Contact {
    address: i32,
    uname: String
}
