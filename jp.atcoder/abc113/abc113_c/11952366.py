import sys
from collections import defaultdict

def fill(s):
    while len(s) < 6: s = '0' + s
    return s

def create_id(p, o):
    return fill(str(p)) + fill(str(o))

n, m, *py = map(int, sys.stdin.read().split())
py = zip(*[iter(py)] * 2)

def main():
    db = defaultdict(list)
    i = 0
    for p, y in py:
        db[p].append((y, i))
        i += 1

    res = [None] * m
    for p in db:
        db[p].sort()
        for i in range(len(db[p])):
            res[db[p][i][1]] = create_id(p, i + 1)
    print(*res, sep='\n')

if __name__ ==  '__main__':
    main()
