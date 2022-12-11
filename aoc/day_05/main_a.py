import re

from typing.io import BinaryIO


def main_a(fp: BinaryIO):
    stacks = {}
    while line := fp.readline():
        if line.startswith(b' 1'):
            break
        craste = [x for x in line.decode()]
        for i in range(len(craste)):
            print(i)
            if 4 * i + 1 < len(craste):
                if i in stacks and craste[4 * i + 1] != ' ':
                    stacks[i].extend(craste[4 * i + 1])
                elif craste[4 * i + 1] != ' ':
                    stacks[i] = [craste[4 * i + 1]]
    fp.readline()
    while line := fp.readline():
        moves = [int(s) for s in re.findall(r'\b\d+\b', line.decode())]
        popped = []
        for i in range(moves[0]):
            popped.append(stacks[moves[1] - 1].pop(0))
        for i in range(moves[0]):
            stacks[moves[2] - 1].insert(0, popped[i])

    for i in range(len(stacks)):
        print(stacks[i][0])
