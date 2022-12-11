import re

from typing.io import BinaryIO


def main_a(fp: BinaryIO):
    visited_locations = set()
    head_location = [0,0]
    tail_location = [0,0]
    for line in fp.readlines():
        [cmd, dist] = line.decode().split(' ')
        print(line)
        if cmd == 'R':
            for i in range(int(dist)):
                head_location[1] += 1
                if tail_location[1] + 1 < head_location[1]:
                    tail_location[1] += 1
                    if tail_location[0] < head_location[0]:
                        tail_location[0] += 1
                    elif tail_location[0] > head_location[0]:
                        tail_location[0] -= 1
                visited_locations.add(str(tail_location))

        if cmd == 'L':
            for i in range(int(dist)):
                head_location[1] -= 1
                if tail_location[1] - 1 > head_location[1]:
                    tail_location[1] -= 1
                    if tail_location[0] < head_location[0]:
                        tail_location[0] += 1
                    elif tail_location[0] > head_location[0]:
                        tail_location[0] -= 1
                visited_locations.add(str(tail_location))
        if cmd == 'U':
            for i in range(int(dist)):
                head_location[0] += 1
                if tail_location[0] + 1 < head_location[0]:
                    tail_location[0] += 1
                    if tail_location[1] < head_location[1]:
                        tail_location[1] += 1
                    elif tail_location[1] > head_location[1]:
                        tail_location[1] -= 1
                visited_locations.add(str(tail_location))
        if cmd == 'D':
            for i in range(int(dist)):
                head_location[0] -= 1
                if tail_location[0] - 1 > head_location[0]:
                    tail_location[0] -= 1
                    if tail_location[1] < head_location[1]:
                        tail_location[1] += 1
                    elif tail_location[1] > head_location[1]:
                        tail_location[1] -= 1
                visited_locations.add(str(tail_location))
        print(head_location)
        print(tail_location)
        print(len(visited_locations))