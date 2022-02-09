import sys

n, g, *pc = map(int, sys.stdin.read().split())
p, c = pc[::2], pc[1::2]
s = [100 * (i + 1) for i in range(n)]

def main():
    res = float('inf')
    for i in range(1 << n):
        tot = 0
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                cnt += p[j]
                tot += s[j] * p[j] + c[j]
            else:
                k = j
        if tot >= g: res = min(res, cnt); continue
        d = (g - tot + s[k] - 1) // s[k]
        if d < p[k]: res = min(res, cnt + d)
    print(res)

if __name__ ==  '__main__':
    main()
