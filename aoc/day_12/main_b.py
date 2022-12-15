from collections import deque

from typing.io import BinaryIO

import numpy


def plan(st, network, end):
    q = deque()
    q.append((st, 0))
    seen = set()
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                    0 <= x + dx < len(network)
                    and 0 <= y + dy < len(network[0])
                    and network[x + dx][y + dy] - network[x][y] <= 1
            ):
                q.append(((x + dx, y + dy), dist + 1))
    return float("inf")

def main_b(fp: BinaryIO):
    data = fp.readlines()
    network = []
    for i in range(len(data)):
        network.append([])
        network[i] = [c - 96 if c >= 97 else 1 if c == 83 else 27 for c in data[i].strip()]

    network = numpy.array(network)

    sts = numpy.where(network == 1)
    end = numpy.where(network == 27)
    end = (end[0][0], end[1][0])
    dists = [plan((sts[0][st], sts[1][st]), network, end) for st in range(len(sts[0]))]
    dists.sort()
    print(dists[0])

