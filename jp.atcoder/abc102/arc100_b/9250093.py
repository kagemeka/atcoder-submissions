import sys
from itertools import accumulate

n, *a = map(int, sys.stdin.read().split())

def main():
    ans = float('inf')
    left = 0; right = 2
    p = a[0]; q = 0; r = sum(a[1:3]); s = sum(a[3:])
    for c in range(1, n-2):
        q += a[c]; r -= a[c]
        while left < c - 1:
            nex = a[left+1]
            if abs((q - nex) - (p + nex)) <= abs(q - p):
                q -= nex; p += nex
                left += 1
            else:
                break

        while right < n - 2:
            nex = a[right+1]
            if abs((s - nex) - (r + nex)) <= abs(s - r):
                s -= nex; r += nex
                right += 1
            else:
                break

        res = sorted([p, q, r, s])
        ans = min(ans, res[-1] - res[0])

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
