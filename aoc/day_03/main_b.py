import string

from typing.io import BinaryIO

ap = string.ascii_letters


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def main_b(fp: BinaryIO):
    t = 0
    for lines in divide_chunks(fp.readlines(), 3):
        chars_first = set(string.ascii_letters)
        for line in lines:
            chars_second = set(line.decode())
            chars_first = chars_first.intersection(chars_second)
        t += ap.index(chars_first.pop()) + 1

    print(t)
