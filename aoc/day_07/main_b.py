import re

from typing.io import BinaryIO


def get_storage_size(item, storage):
    size = 0
    for folder in item['folders']:
        size += get_storage_size(storage[folder], storage)
    return size + item['size']


def main_b(fp: BinaryIO):
    storage = {}
    current_folder = '/'
    for line in fp.readlines():
        cmd = line.decode()
        if cmd.startswith('$ cd'):
            [_, _, folder] = cmd.strip().split(' ')
            if folder == '..':
                parts = current_folder.split('/')
                current_folder = '/'.join(parts[:-2]) + '/'
            else:
                current_folder += folder + '/'
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
    c = 0
    folders = []
    for key, item in storage.items():
        folders.append({'size': item['size'], 'key': key})
        if item['size'] <= 100000:
            c += item['size']
    print('A')
    print(c) # A done
    folders.sort(key=lambda x: x['size'])

    limit = folders[-1]['size'] - 40000000
    for folder in folders:
        if folder['size'] >= limit:
            print(folder['size'])
            break
