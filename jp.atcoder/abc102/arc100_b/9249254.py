import sys
from itertools import accumulate
from bisect import bisect_left as bi_l

n, *a = map(int, sys.stdin.read().split())

def main():
    s = list(accumulate(a))

    ans = float('inf')
    for center in range(1, n-2):
        pq = s[center]
        left = bi_l(s, pq / 2)
        if left == 0:
            p = s[0]
        else:
            if pq - s[left] < s[left-1]:
                left -= 1
            p = s[left]
        q = pq - p

        rt = s[-1] - pq
        right = bi_l(s, pq + rt / 2)
        if right == center + 1:
            r = s[center+1] - pq
        else:
            if rt - (s[right] - pq) < s[right-1] - pq:
                right -= 1
            r = s[right] - pq
        t = rt - r

        res = sorted([p, q, r, t])
        ans = min(ans, res[-1] - res[0])

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
