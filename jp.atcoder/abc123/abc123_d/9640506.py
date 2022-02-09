import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r


x, y, z, k = map(int, sys.stdin.readline().split())
a, b, c = (sorted(map(int, sys.stdin.readline().split())) for _ in range(3))

def count_atleast_k(border):
    combs = 0
    for i in range(x):
        for j in range(y):
            combs += z - bi_r(c, border - a[i] - b[j])
    return combs >= k

def main():
    hi = 3 * 10 ** 10 + 1
    lo = 2
    while lo + 1 < hi:
        border = (lo + hi) // 2
        if count_atleast_k(border):
            lo = border
        else:
            hi = border

    res = []
    for i in range(x-1, -1, -1):
        if hi - a[i] > b[-1] + c[-1]:
            break
        for j in range(y-1, -1, -1):
            if hi - a[i] - b[j] > c[-1]:
                break
            for k in range(z-1, -1, -1):
                if hi - a[i] - b[j] - c[k] > 0:
                    break
                res.append(a[i] + b[j] + c[k])

    return sorted(res, reverse=True)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
