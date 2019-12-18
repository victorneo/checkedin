from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


KEY_SIZE = 2048


def get_rsa_private_key_in_pem_bytes(key):
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )


def get_rsa_public_key_in_pem_bytes(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)


def generate_rsa_key_pair():
    """Generates a RSA public and private key pair in bytes."""
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=KEY_SIZE,
        backend=default_backend()
    )

    priv_key = get_rsa_private_key_in_pem_bytes(key)
    pub_key = get_rsa_public_key_in_pem_bytes(key.public_key())

    return priv_key, pub_key


def get_rsa_private_key_from_pem_string(priv_key):
    return serialization.load_pem_private_key(
            priv_key.encode(),
            password=None,
            backend=default_backend())


def get_rsa_public_key_from_pem_string(pub_key):
    return serialization.load_pem_public_key(
            pub_key.encode(), backend=default_backend())
