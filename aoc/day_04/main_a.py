from typing.io import BinaryIO


def main_a(fp: BinaryIO):
    # c = 0
    # for line in fp.readlines():
    #     pair_1, pair_2 = line.strip().decode().split(',')
    #     pair_1_0, pair_1_1 = pair_1.split('-')
    #     pair_2_0, pair_2_1 = pair_2.split('-')
    #     print(f'{pair_1_0} {pair_2_0} && {pair_1_1} {pair_2_1}')
    #     if int(pair_1_0) <= int(pair_2_0) and int(pair_2_1) <= int(pair_1_1):
    #         print('me')
    #         c+=1
    #     elif int(pair_2_0) <= int(pair_1_0) and int(pair_1_1) <= int(pair_2_1):
    #         print('other')
    #         c+=1
    #
    #
    #
    # print(c)

    p1 = 0
    p2 = 0

    for line in fp.readlines():
        line = line.decode()
        if not line: continue
        ra, rb = line.split(',')
        raa, rab = map(int, ra.split('-'))
        rba, rbb = map(int, rb.split('-'))

        if (raa <= rba and rbb <= rab) or (rba <= raa and rab <= rbb):
            p1 += 1

        rA = set(range(raa, rab + 1))
        rB = set(range(rba, rbb + 1))
        if rA & rB:
            p2 += 1

    print(p1)
    print(p2)