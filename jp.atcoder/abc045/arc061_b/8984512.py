import sys
from collections import defaultdict, Counter

h, w, n = map(int, sys.stdin.readline().split())
ab = map(int, sys.stdin.read().split())
ab = zip(ab, ab)

def main():
    c = defaultdict(int)
    for a, b in ab:
        for da in range(-2, 1):
            for db in range(-2, 1):
                # 今見ているマスを含むrectangularの左上
                i = a + da
                j = b + db
                if 1 <= i <= h - 2 and 1 <= j <= w - 2:
                    c[(i, j)] += 1

    res = Counter(c.values())
    cnt_0 = (h - 2) * (w - 2) - sum(res.values())
    yield cnt_0
    for i in range(1, 10):
        if i in res:
            yield res[i]
        else:
            yield 0

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
