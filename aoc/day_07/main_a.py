import re

from typing.io import BinaryIO


def get_storage_size(item, storage):
    size = 0
    for folder in item['folders']:
        size += get_storage_size(storage[folder], storage)
    return size + item['size']

def main_a(fp: BinaryIO):
    storage = {}
    current_folder = '/'
    previous_folder = '/'
    for line in fp.readlines():
        cmd = line.decode()
        if cmd.startswith('$ cd'):
            print(cmd)
            [_, _, folder] = cmd.strip().split(' ')
            if folder == '..':
                parts = current_folder.split('/')
                print(parts)
                current_folder = '/'.join(parts[:-2]) + '/'
                print(current_folder)
            else:
                current_folder += folder + '/'
                print(current_folder)
                storage[current_folder] = {'folders': [], 'size': 0}
        elif cmd.startswith('$ ls'):
            pass
        elif cmd.startswith('dir'):
            [_, folder] = cmd.strip().split(' ')
            storage[current_folder]['folders'].append(current_folder + folder + '/')
        else:
            [size, _] = cmd.strip().split(' ')
            storage[current_folder]['size'] += int(size)
    print(storage)
    for key, item in storage.items():
        storage[key]['size'] = get_storage_size(item, storage)
        print(key)
        print(storage[key]['size'])
    c = 0
    for key, item in storage.items():
        if item['size'] <= 100000:
            c += item['size']
    print(c)