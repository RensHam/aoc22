import textwrap

from typing.io import BinaryIO

def calc_char(t, x):
    if x - 1 <= (t % 40) <= x+1:
        return '#'
    return '.'

def main_b(fp: BinaryIO):
    x = 1
    t = 0
    value = ''
    for line in fp.readlines():
        value += calc_char(t, x)
        t += 1
        if b'addx' in line:
            [_, num] = line.split(b' ')
            value += calc_char(t, x)
            t += 1
            x += int(num)
    print('\n'.join(textwrap.wrap(value, 40)))




