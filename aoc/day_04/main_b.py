from typing.io import BinaryIO


def main_b(fp: BinaryIO):
    c = 0
    for line in fp.readlines():
        pair_1, pair_2 = line.strip().decode().split(',')
        pair_1_0, pair_1_1 = pair_1.split('-')
        pair_2_0, pair_2_1 = pair_2.split('-')
        if int(pair_2_0) <= int(pair_1_0) <= int(pair_2_1):
            c += 1
        elif int(pair_1_0) <= int(pair_2_0) <= int(pair_1_1):
            c += 1
        elif int(pair_2_0) <= int(pair_1_1) <= int(pair_2_1):
            c += 1
        elif int(pair_1_0) <= int(pair_2_1) <= int(pair_1_1):
            c += 1
    print(c)