import sys
from math import floor, sqrt, ceil

q, *ab = map(int, sys.stdin.read().split())
ab = zip(*[iter(ab)] * 2)

def main():
    for a, b in ab:
        if a > b:
            a, b = b, a
        res = 0
        res += (a - 1) * 2

        if b - a <= 1:
            yield res
            continue

        s = a * b
        res += (floor(sqrt(s - 1)) - a) * 2 + 1
        if floor(sqrt(s - 1)) ** 2 == s - 1:
            res -= 1
        yield res
        continue

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
