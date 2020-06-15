import string

ALL_CHARACTERS = string.printable
TOTAL_CHARACTERS = len(ALL_CHARACTERS)

def char_to_label(string_):
    return list(map(lambda c: ALL_CHARACTERS.find(c), string_))

print char_to_label("hello my name is jony")