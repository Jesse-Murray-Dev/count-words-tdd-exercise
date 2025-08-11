from lib.count_words import *

def test_count_words():
    assert count_words("This string has five words") == 5
    assert count_words("hello") == 1