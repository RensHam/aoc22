from typing.io import BinaryIO

MAPPING_OPT = {
    'A': 0,  # ROCK
    'B': 1,  # PAPER
    'C': 2,  # SCISSORS
    'X': 0,  # ROCK
    'Y': 1,  # PAPER
    'Z': 2,  # SCISSORS
}

SCORE = {
    'X': 1,  # ROCK
    'Y': 2,  # PAPER
    'Z': 3,  # SCISSORS
}

SCORE_2 = {
    'X': 0,  # LOOSE
    'Y': 3,  # DRAW
    'Z': 6,  # WIN
}

# 'A' < 'B'
# 'B' < 'C'
# 'C' < 'A'

def day_02_main(fp: BinaryIO):
    score = 0
    for line in fp.readlines():
        f = line.decode()
        elf = f[0]
        me = f[2]
        points = SCORE[me]
        if MAPPING_OPT[elf] == MAPPING_OPT[me]:
            score += 3
        elf = MAPPING_OPT[elf]

        me = 1
        if elf == 0 and me == 1:
            score += 6
        if elf == 1 and me == 2:
            score += 6
        if elf == 2 and me == 0:
            score += 6
            print(points)

        score += points
        score += me

    print(score)


def day_02_main_b(fp: BinaryIO):
    score = 0
    for line in fp.readlines():
        f = line.decode()
        elf = f[0]
        me = f[2]
        points = SCORE_2[me]
        # if MAPPING_OPT[elf] == MAPPING_OPT[me]:
        #     score += 3
        elf = MAPPING_OPT[elf]
        if points == 0:
            me = elf
            if me == 0:
                me = 3
        elif points == 3:
            me = elf + 1
        elif points == 6:
            me = elf + 2
            if me == 4:
                me = 1

        score += points
        score += me
    print(score)
