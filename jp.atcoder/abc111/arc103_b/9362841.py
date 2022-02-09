import sys

n = int(sys.stdin.readline().rstrip())
xy = list(zip(*[map(int, sys.stdin.read().split())] * 2))

mask = (1 << 31) - 1
def solve(x, y, mode):
    u = x + y
    v = x - y
    if mode == 0:
        u -= 1
        v -= 1

    s = (u + mask) >> 1
    t = (v + mask) >> 1

    l = (~(s | t)) & mask
    r = s & t & mask
    d = (~s) & t & mask
    u = s & (~t) & mask

    res = ''
    for i in range(31):
        if l >> i & 1:
            res += 'L'
        elif r >> i & 1:
            res += 'R'
        elif d >> i & 1:
            res += 'D'
        elif u >> i & 1:
            res += 'U'
    if mode == 0:
        res += 'R'

    return [res]

def main():
    oe = (xy[0][0] + xy[0][1]) % 2
    for x, y in xy:
        if (x + y) % 2 != oe:
            print(-1)
            sys.exit()

    m = 31
    d = [2 ** i for i in range(31)]
    if oe == 0:
        d += [1]
        m += 1
    yield [m]
    yield d

    for x, y in xy:
        yield solve(x, y, oe)

if __name__ == '__main__':
    ans = main()
    for i in ans:
        print(*i, sep=' ')
