import json
from functools import cmp_to_key

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


def main_b(fp: BinaryIO):
    total = 0
    i = 1
    messages = []
    while (left := fp.readline()) != b'':
        messages.append(json.loads(left))
        messages.append(json.loads(fp.readline()))
        fp.readline()

    messages.append(2)
    messages.append(6)
    messages.sort(key=cmp_to_key(check_item), reverse=True)
    for m in messages:
        if m == 2:
            total = i
        if m == 6:
            total *= i
        i += 1

    print(total)






