from scripts.codingbat import string_bits # string_bits is file

def test_return_string():
    assert string_bits.return_string("z") == "z"

def test_string_bits():
    assert string_bits.string_bits("Hello") == "Hlo"

    # must start function name as test_ or wont work (e.g. string_bits_refactor1 must be test_string_bits_refactor1)
def test_string_bits_refactor1():
    assert string_bits.string_bits_refactor1("Hello") == "Hlo"