import re

from typing.io import BinaryIO


def main_a(fp: BinaryIO):
    line = fp.readline()
    i = 0
    while True:
        chars = line[i: i+4]
        if len(set(chars)) == 4:
            print(i + 4)
            break
        i += 1