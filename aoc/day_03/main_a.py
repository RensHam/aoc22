import string

from typing.io import BinaryIO

ap = string.ascii_letters


def main_a(fp: BinaryIO):
    t = 0
    for line in fp.readlines():
        strings = line.decode()
        firstpart, secondpart = strings[:len(strings) // 2], strings[len(strings) // 2:]
        chars_first = set(firstpart)
        chars_second = set(secondpart)
        t += ap.index(chars_first.intersection(chars_second).pop()) + 1

    print(t)
