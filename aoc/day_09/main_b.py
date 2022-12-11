import re

from typing.io import BinaryIO


def move_tail(head_location, tail_location):
    if tail_location[1] + 1 < head_location[1]:
        tail_location[1] += 1
        if tail_location[0] < head_location[0]:
            tail_location[0] += 1
        elif tail_location[0] > head_location[0]:
            tail_location[0] -= 1
        return tail_location
    if tail_location[1] - 1 > head_location[1]:
        tail_location[1] -= 1
        if tail_location[0] < head_location[0]:
            tail_location[0] += 1
        elif tail_location[0] > head_location[0]:
            tail_location[0] -= 1
        return tail_location
    if tail_location[0] + 1 < head_location[0]:
        tail_location[0] += 1
        if tail_location[1] < head_location[1]:
            tail_location[1] += 1
        elif tail_location[1] > head_location[1]:
            tail_location[1] -= 1
        return tail_location
    if tail_location[0] - 1 > head_location[0]:
        tail_location[0] -= 1
        if tail_location[1] < head_location[1]:
            tail_location[1] += 1
        elif tail_location[1] > head_location[1]:
            tail_location[1] -= 1
        return tail_location
    return tail_location


def main_b(fp: BinaryIO):
    visited_locations = set()
    head_location = [0, 0]
    tail_locations = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for line in fp.readlines():
        [cmd, dist] = line.decode().split(' ')
        print(line)
        if cmd == 'R':
            for i in range(int(dist)):
                head_location[1] += 1
                tail_locations[0] = move_tail(head_location, tail_locations[0])
                for i in range(1, len(tail_locations)):
                    tail_locations[i] = move_tail(tail_locations[i - 1], tail_locations[i])
                visited_locations.add(str(tail_locations[-1]))

        if cmd == 'L':
            for i in range(int(dist)):
                head_location[1] -= 1
                tail_locations[0] = move_tail(head_location, tail_locations[0])
                for i in range(1, len(tail_locations)):
                    tail_locations[i] = move_tail(tail_locations[i - 1], tail_locations[i])
                visited_locations.add(str(tail_locations[-1]))
        if cmd == 'U':
            for i in range(int(dist)):
                head_location[0] += 1
                tail_locations[0] = move_tail(head_location, tail_locations[0])
                for i in range(1, len(tail_locations)):
                    tail_locations[i] = move_tail(tail_locations[i - 1], tail_locations[i])
                visited_locations.add(str(tail_locations[-1]))
        if cmd == 'D':
            for i in range(int(dist)):
                head_location[0] -= 1
                tail_locations[0] = move_tail(head_location, tail_locations[0])
                for i in range(1, len(tail_locations)):
                    tail_locations[i] = move_tail(tail_locations[i - 1], tail_locations[i])
                visited_locations.add(str(tail_locations[-1]))
        print(len(visited_locations))
