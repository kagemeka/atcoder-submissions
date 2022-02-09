import sys

n, g, *pc = map(int, sys.stdin.read().split())
p, c = pc[::2], pc[1::2]

def main():
    res = float('inf')
    for i in range(1 << n):
        tot = 0
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                cnt += p[j]
                tot += 100 * (j + 1) * p[j] + c[j]
            else:
                k = j
        if tot >= g: res = min(res, cnt); continue
        d = (g - tot + 100 * (k + 1) - 1) // (100 * (k + 1))
        if d < p[k]: res = min(res, cnt + d)
    print(res)

if __name__ ==  '__main__':
    main()
