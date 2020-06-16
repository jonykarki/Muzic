# test_utils.py
import utils
import string

def test_get_total_characters():
    assert(utils.get_total_characters() == len(string.printable))

def test_char_to_label():
    assert(utils.char_to_label("Hello") == [43, 14, 21, 21, 24])