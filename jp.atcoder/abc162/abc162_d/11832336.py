import sys
from bisect import bisect_right as bi_r, bisect_left as bi_l

n, s = sys.stdin.read().split()
n = int(n)
s = s.replace('R', '0')
s = s.replace('G', '1')
s = s.replace('B', '2')
s = [int(x) for x in s]

def main():
    res = [[] for _ in range(3)]
    for i in range(n):
        res[s[i]].append(i)
    tot = 0
    for j in range(1, n - 1):
        cnt = 0
        m = s[j]
        if m == 0:
            lr = [(1, 2), (2, 1)]
        elif m == 1:
            lr = [(0, 2), (2, 0)]
        else:
            lr = [(0, 1), (1, 0)]
        for l, r in lr:
            cnt += bi_r(res[l], j) * (len(res[r]) - bi_l(res[r], j))
        i = j - 1
        k = j + 1
        while True:
            if i < 0 or k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                cnt -= 1
            i -= 1
            k += 1
        tot += cnt
    print(tot)

if __name__ ==  '__main__':
    main()
