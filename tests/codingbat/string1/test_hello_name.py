from scripts.codingbat.string1.hello_name import hello_name

def test_hello_name():
    assert hello_name("Bob") == "Hello Bob!"
    assert hello_name("X") == "Hello X!"