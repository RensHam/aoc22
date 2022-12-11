import re

from typing.io import BinaryIO


def main_b(fp: BinaryIO):
    line = fp.readline()
    # line = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    i = 0
    while True:
        chars = line[i: i+14]
        if len(set(chars)) == 14:
            print(i + 14)
            break
        # elif i > 20:
        #     break
        i += 1