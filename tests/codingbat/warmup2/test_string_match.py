from scripts.codingbat.warmup2 import string_match

def test_string_match():
    assert string_match.string_match('xxcaazz', 'xxbaaz') == \
        3

def test_string_match2():
    assert string_match.string_match('abc', 'abc') == 2

def test_string_match3():
    assert string_match.string_match('abc', 'axc') == 0