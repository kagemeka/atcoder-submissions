import sys
from itertools import accumulate

n, m, *a = map(int, sys.stdin.read().split())
a.sort()

ma = a[-1]
cnt = [0] * (ma + 1)
cur = ma
for i in range(n-1, -1, -1):
    if a[i] == cur:
        cnt[cur] += 1
    else:
        while True:
            cur -= 1
            cnt[cur] = cnt[cur+1]
            if cur == a[i]:
                cnt[cur] += 1
                break
for i in range(cur-1, -1, -1):
    cnt[i] = cnt[i+1]


def possible(border):
    pair_cnt = 0
    for i in range(n):
        aj = border - a[i]
        if aj < 0:
            aj = 0
        elif aj > ma:
            continue
        pair_cnt += cnt[aj]
    return pair_cnt >= m

def main():
    s = [0] + list(accumulate(a[::-1]))

    lo = 1; hi = a[-1] * 2 + 1
    while lo + 1 < hi:
        border = (lo + hi) // 2
        if possible(border):
            lo = border
        else:
            hi = border
    res = lo
    ans = 0
    minimum = float('inf')
    pair_cnt = 0
    for i in range(n):
        aj = res - a[i]
        if aj < 0:
            aj = 0
        elif aj > ma:
            continue
        c = cnt[aj]
        ans += s[c] + a[i] * c
        pair_cnt += c
        minimum = min(minimum, a[i] + a[-c])

    ans -= minimum * (pair_cnt - m)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
