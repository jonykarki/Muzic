# test_utils.py
import utils

def test_char_to_label():
    assert(utils.char_to_label("Hello") == [43, 14, 21, 21, 24])