from encrypt import encrypt_word
from decrypt import decrypt_word


def test_encrypt_decrypt_just_text_all_lower():
    message = "helloworld"
    key, cypher_text = encrypt_word(message)
    output = decrypt_word(key, cypher_text)

    assert message == output
    assert message != cypher_text

def test_encrypt_decrypt_just_text_upper_lower():
    message = "HelloWorld"
    key, cypher_text = encrypt_word(message)
    output = decrypt_word(key, cypher_text)

    assert message == output
    assert message != cypher_text

def test_encrypt_decrypt_text_spaces():
    message = "Hello World"
    key, cypher_text = encrypt_word(message)
    output = decrypt_word(key, cypher_text)

    assert message == output
    assert message != cypher_text

def test_encrypt_decrypt_alphanum():
    message = "Hello World 123"
    key, cypher_text = encrypt_word(message)
    output = decrypt_word(key, cypher_text)

    assert message == output
    assert message != cypher_text

def test_encrypt_decrypt_alphanum_symbols():
    message = "Hello World! 123 #$*"
    key, cypher_text = encrypt_word(message)
    output = decrypt_word(key, cypher_text)

    assert message == output
    assert message != cypher_text