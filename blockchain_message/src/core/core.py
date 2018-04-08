class Message (object):
    def __init__(self, id, to, fr, text):
        self.id = id
        self.to = to
        self.fr = fr
        self.text = text


class Contact (object):
    def __init__(self, address, uname, email):
        self.address = address
        self.uname = uname
        self.email = email
