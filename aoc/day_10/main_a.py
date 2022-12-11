from typing.io import BinaryIO

def check_time_value(t , x):
    if (t + 20) % 40 == 0:
        return x * t
    return 0


def main_a(fp: BinaryIO):
    x = 1
    t = 0
    value = 0
    for line in fp.readlines():
        value += check_time_value(t, x)
        t += 1
        if b'addx' in line:
            [_, num] = line.split(b' ')
            value += check_time_value(t, x)
            t += 1
            x += int(num)
    print(value)


