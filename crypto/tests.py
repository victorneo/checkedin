from unittest.mock import MagicMock, patch
from crypto.rsa_utils import (
        generate_rsa_key_pair,
        get_rsa_private_key_from_pem_string,
        get_rsa_public_key_from_pem_string,
        get_rsa_private_key_in_pem_bytes,
        get_rsa_public_key_in_pem_bytes)


@patch('crypto.rsa_utils.rsa')
def test_generate_rsa_key_pair(rsa):
    mock_key = MagicMock()
    rsa.generate_private_key.return_value = mock_key

    priv, pub = generate_rsa_key_pair()

    rsa.generate_private_key.assert_called()
    mock_key.private_bytes.assert_called()
    mock_key.public_key.assert_called()
    mock_key.public_key().public_bytes.assert_called()

    assert priv == mock_key.private_bytes()
    assert pub == mock_key.public_key().public_bytes()


def test_rsa_key_from_string():
    from crypto.rsa_utils import KEY_SIZE
    ORIG_KEY_SIZE = KEY_SIZE
    KEY_SIZE = 128
    # Generate a real rsa key pair with small key size for testing
    priv, pub = generate_rsa_key_pair()

    restored_priv = get_rsa_private_key_from_pem_string(priv.decode())
    assert priv.decode() == \
            get_rsa_private_key_in_pem_bytes(restored_priv).decode()

    restored_pub = get_rsa_public_key_from_pem_string(pub.decode())
    assert pub.decode() == \
            get_rsa_public_key_in_pem_bytes(restored_pub).decode()

    KEY_SIZE  = ORIG_KEY_SIZE
