import json

from typing.io import BinaryIO


def check_item(left, right):
    if type(left) == list or type(right) == list:
        if not(type(left) == list):
            left = [left]
        if not(type(right) == list):
            right = [right]
        for left_item, right_item in zip(left, right):
            if (check := check_item(left_item, right_item)) != 0:
                return check
        if len(left) < len(right):
            return 1
        if len(right) < len(left):
            return -1
        return 0

    if left < right:
        return 1
    if left == right:
        return 0
    return -1






def main_a(fp: BinaryIO):
    total = 0
    i = 1
    while (left := fp.readline()) != b'':
        left = json.loads(left)
        right = json.loads(fp.readline())
        fp.readline()
        if check_item(left, right) > 0:
            total += i
            print(i)
        i += 1

    print(total)






