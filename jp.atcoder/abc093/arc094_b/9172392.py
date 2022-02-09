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

        p = a * b
        c = floor(sqrt(p))
        res += (c - a) * 2 + 1
        if c * (c + 1) >= p:
            res -= 1
        if c * c == p:
            res -= 1
        yield res



if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
