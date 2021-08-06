from scripts.codingbat import string_bits

def test_return_string():
    assert string_bits.return_string("z") == "z"

def test_string_bits():
    assert string_bits.string_bits("Hello") == "Hlo"