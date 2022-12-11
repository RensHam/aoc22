import numpy


def main_a(f):
    data = numpy.genfromtxt(f, delimiter=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,])
    count = 0
    tree_seen = 2*99 + 2*97
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i, :]) - 1):
            tree = data[i, j]
            if max(data[:i, j]) < tree:
                tree_seen += 1
            elif max(data[i, :j]) < tree:
                tree_seen += 1
            elif max(data[i+1:, j]) < tree:
                tree_seen += 1
            elif max(data[i, j+1:]) < tree:
                tree_seen += 1
            else:
                count += 1
        print(f"{i} - {j}")
    print(count)
    print(tree_seen)
