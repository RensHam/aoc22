import numpy

def calc(left_trees):
    tmp_s = 0
    for t in left_trees:
        if not t:
            break
        tmp_s += 1
    if len(left_trees) > 1:
        tmp_s += 1
        tmp_s = min(len(left_trees), tmp_s)
    else:
        tmp_s = 1
    return tmp_s

def main_b(f):
    data = numpy.genfromtxt(f, delimiter=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,])
    senic = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i, :]) - 1):
            tree = data[i, j]
            tmp_s = calc((data[:i, j] < tree)[::-1])
            tmp_s *= calc((data[i, :j] < tree)[::-1])
            tmp_s *= calc(data[i + 1:, j] < tree)
            tmp_s *= calc(data[i, j + 1:] < tree)
            senic = max(tmp_s, senic)
    print(senic)
