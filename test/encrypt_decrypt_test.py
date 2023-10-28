from main.encrypt import encryptFunction
from main.decrypt import decryptFunction


def test_encrypt_decrypt_just_text_all_lower():
    message = "helloworld"
    key, cypher_text = encryptFunction(message)
    output = decryptFunction(key, cypher_text)

    assert message == output
    assert message != cypher_text

def test_encrypt_decrypt_just_text_upper_lower():
    message = "HelloWorld"

def test_encrypt_decrypt_text_spaces():
    message = "Hello World"

def test_encrypt_decrypt_alphanum():
    message = "Hello World 123"

def test_encrypt_decrypt_alphanum_symbols():
    message = "Hello World! 123 #$*"