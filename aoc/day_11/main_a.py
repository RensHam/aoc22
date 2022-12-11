from typing import Callable

from typing.io import BinaryIO

class Monkey:
    def __init__(self, items: list[int], operation: Callable, testing: Callable, target_true, target_false):
        self._items = items
        self._operation = operation
        self._test = testing
        self.target_true_num = target_true
        self.target_false_num = target_false
        self._target_true: 'Monkey' | None = None
        self._target_false: 'Monkey' | None = None
        self._inspected_items = 0

    def run(self):
        for item in self._items:
            self._inspected_items += 1
            item = int(self._operation(item) / 3)
            if self._test(item):
                self._target_true.catch(item)
            else:
                self._target_false.catch(item)

        self._items = []

    def catch(self, item: int):
        self._items.append(item)

    def link_true_monkey(self, monkey: 'Monkey'):
        self._target_true = monkey

    def link_false_monkey(self, monkey: 'Monkey'):
        self._target_false = monkey

    @property
    def inspected_items(self):
        return self._inspected_items

def create_new_function(line):
    [_, _, _, _, operation, fixed_num] = line.strip().split(' ')
    if fixed_num.isdigit():
        fixed_num = int(fixed_num)
    else:
        fixed_num = None

    def adder_fixed_num(item):
        return item + fixed_num

    def multi_fixed_num(item):
        return item * fixed_num

    def square(item):
        return item * item

    if fixed_num is None:
        return square
    if '+' in operation:
        return adder_fixed_num
    return multi_fixed_num

def create_test_function(test_line):
    divider = int(test_line.split(' ')[-1])

    def test_fn(item):
        return item % divider == 0

    return test_fn


def parse_monkey(fp: BinaryIO):
    if fp.readline() == b'':
        return False
    items = list(map(int, (fp.readline().split(b': ')[1]).strip().split(b', ')))
    operation = create_new_function(fp.readline().decode())
    test_fn = create_test_function(fp.readline().decode())
    monkey_true = int(fp.readline().decode().split(' ')[-1])
    monkey_false = int(fp.readline().decode().split(' ')[-1])
    fp.readline()
    return Monkey(
        items,
        operation,
        test_fn,
        monkey_true,
        monkey_false,
    )


def main_a(fp: BinaryIO):
    monkeys = []
    while monkey := parse_monkey(fp):
        monkeys.append(monkey)
    for i in range(0, len(monkeys)):
        monkeys[i].link_true_monkey(
            monkeys[monkeys[i].target_true_num]
        )
        monkeys[i].link_false_monkey(
            monkeys[monkeys[i].target_false_num]
        )
    for _ in range(20):
        for monkey in monkeys:
            monkey.run()

        # if _ == 1:
        #     for monkey in monkeys:
        #         print(monkey.inspected_items)

    num_items = [monkey.inspected_items for monkey in monkeys]
    num_items.sort()
    print(num_items[-2] * num_items[-1])
    for monkey in monkeys:
        print(monkey.inspected_items)
