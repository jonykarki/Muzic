import string
import subprocess

ALL_CHARACTERS = string.printable
TOTAL_CHARACTERS = len(ALL_CHARACTERS)

def get_total_characters():
    return TOTAL_CHARACTERS

def char_to_label(string_):
    return list(map(lambda c: ALL_CHARACTERS.find(c), string_))