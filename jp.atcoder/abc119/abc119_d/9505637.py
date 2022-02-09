import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r

inf = float('inf')

a, b, q = map(int, sys.stdin.readline().split())
*I, = map(int, sys.stdin.read().split())
s = I[:a]
t = I[a:a+b]
X = I[a+b:]

def main():
    for x in X:
        ls = bi_r(s, x) - 1
        rs = bi_l(s, x)
        lt = bi_r(t, x) - 1
        rt = bi_l(t, x)
        dls = s[ls] - x if ls >= 0 else -inf
        drs = s[rs] - x if rs <= a - 1 else inf
        dlt = t[lt] - x if lt >= 0 else -inf
        drt = t[rt] - x if rt <= b - 1 else inf

        res = inf
        for ds in [dls, drs]:
            for dt in [dlt, drt]:
                if ds * dt > 0:
                    d = max(abs(ds), abs(dt))
                else:
                    ds = abs(ds)
                    dt = abs(dt)
                    d = min(ds, dt) * 2 + max(ds, dt)
                res = min(res, d)
        yield res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
