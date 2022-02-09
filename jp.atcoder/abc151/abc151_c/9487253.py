import sys

n, m = map(int, sys.stdin.readline().split())
pv = []
for _ in range(m):
    p, v = sys.stdin.readline().split()
    p = int(p)
    v = 1 if v == 'AC' else 0
    pv.append((p, v))

def main():
    ac = [0] * (n + 1)
    wa = [0] * (n + 1)
    for p, v in pv:
        wa[p] += (ac[p] | v) ^ 1
        ac[p] |= v

    for p in range(1, n+1):
        wa[p] *= ac[p]

    return sum(ac), sum(wa)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
