from typing.io import BinaryIO



def day_01_main(fp: BinaryIO):
    count = 0
    elfs = []
    for food in fp.readlines():
        if food != b'\n':
            count += int(food)
        else:
            elfs.append(count)
            count = 0
    elfs.sort()
    print(elfs)


def day_01_main_b(fp: BinaryIO):
    count = 0
    max_count_1 = 0
    max_count_2 = 0
    max_count_3 = 0
    lines = fp.read().decode()
    elfs = lines.split('\n\n')
    for elf in elfs:
        foods = elf.split('\n')
        for food in foods:
            count += int(food)
        if count > max_count_1:
            tmp = max_count_1
            max_count_1 = count
            count = tmp
        if count > max_count_2:
            tmp = max_count_2
            max_count_2 = count
            count = tmp
        if count > max_count_3:
            max_count_3 = count
        count = 0

    print(max_count_1 + max_count_2 + max_count_3)