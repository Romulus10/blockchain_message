use gpgme;
use gpgme::{Context, Protocol};

pub struct Crypt {
    our_key: String,
}

impl Crypt {
    //! # mod crypt
    //! Allows specialized access to RSA functions.
    pub fn new(identity: String) -> Crypt {
        Crypt {
            our_key: identity,
        }
    }

    pub fn sign(&self, clear: String) -> String {
        //! ## sign(clear: String, key: String) -> String
        //! Takes plaintext and our public key, and signs the plaintext.
        //! Returns the produced signature.
        let proto = Protocol::OpenPgp;
        let mode = gpgme::SignMode::Clear;
        let mut ctx = Context::from_protocol(proto).unwrap();
        ctx.set_armor(true);
        let key = ctx.find_secret_key(self.our_key.clone()).unwrap();
        ctx.add_signer(&key).unwrap();
        let mut output = Vec::new();
        ctx.sign(mode, clear, &mut output).expect("signing failed");
        String::from_utf8(output).unwrap()
    }

#[allow(unused_must_use)]
    pub fn verify(&self, sig: String) -> String {
        //! ## verify(sig: String) -> String
        //! Takes a signature string and verifies it against our known public keys.
        //! Returns the verified status.
        let proto = Protocol::OpenPgp;
        let mut ctx = Context::from_protocol(proto).unwrap();
        let mut output = Vec::new();
        ctx.verify_opaque(sig, &mut output); // The unused_must_used is for this... we really don't care about the Result.
        String::from_utf8(output).unwrap()
    }

    pub fn encrypt(&self, clear: String) -> String {
        //! ## encrypt(clear: String, us: String) -> String
        //! Takes a plaintext string and our private key fingerprint, then encrypts the plaintext with our public key.
        //! Returns the encrypted string.
        let proto = Protocol::OpenPgp;
        let mut ctx = Context::from_protocol(proto).unwrap();
        ctx.set_armor(true);
        let mut recipients = Vec::new();
        recipients.push(self.our_key.clone());
        let keys: Vec<gpgme::Key> = ctx.find_keys(recipients).unwrap().filter_map(Result::ok).filter(|k| k.can_encrypt()).collect();
        let mut output = Vec::new();
        ctx.encrypt(&keys, clear, &mut output).expect("encrypting failed");
        String::from_utf8(output).unwrap()
    }

    pub fn decrypt(&self, cipher: String) -> String {
        //! ## decrypt(cipher: String) -> String
        //! Takes cipher text and decrypts it using our private key.
        //! Returns the decrypted text.
        let proto = Protocol::OpenPgp;
        let mut ctx = Context::from_protocol(proto).unwrap();
        let mut output = Vec::new();
        ctx.decrypt(cipher, &mut output).expect("decrypting failed");
        String::from_utf8(output).unwrap()
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn sign_and_verify() {
        let c = Crypt::new(String::from("test@some-email.io"));
        let x = c.sign(String::from("Test."));
        c.verify(x);
    }

    #[test]
    fn encrypt_and_decrypt() {
        let c = Crypt::new(String::from("test@some-email.io"));
        let x = String::from("Test.");
        let y = c.encrypt(x);
        let z = c.decrypt(String::from(y));
        assert_eq!(String::from("Test."), z);
    }
}
