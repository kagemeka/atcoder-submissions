import sys
from collections import defaultdict

n, m, *py = map(int, sys.stdin.read().split())
py = list(zip(*[iter(py)] * 2))

def main():
    ids = defaultdict(list)
    for p, y in py:
        ids[p].append(y)

    for p, ys in ids.items():
        ids[p] = dict([(y, i) for i, y in enumerate(sorted(ys), 1)])

    for p, y in py:
        x = ids[p][y]
        first = str(p)
        last = str(x)
        first = '0' * (6 - len(first)) + first
        last = '0' * (6 - len(last)) + last
        yield first + last

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
