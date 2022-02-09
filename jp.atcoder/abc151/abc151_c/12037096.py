import sys

n, m = map(int, sys.stdin.readline().split())
pv = []
for _ in range(m):
    p, s = sys.stdin.readline().split()
    p = int(p) - 1
    v = 1 if s == 'AC' else 0
    pv.append((p, v))

def main():
    wa = [0] * n
    ac = [0] * n
    for p, c in pv:
        wa[p] += (ac[p] | v) ^ 1
        ac[p] |= v
    for p in range(n): wa[p] *= ac[p]
    print(sum(ac), sum(wa))

if __name__ ==  '__main__':
    main()
