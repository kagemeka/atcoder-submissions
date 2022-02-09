import sys

sys.setrecursionlimit(10**9)
nCr = {}
def comb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = comb(n-1,r) + comb(n-1,r-1)
    return nCr[(n,r)]

def count(q):
    res = 0
    if q >= 1:
        res += comb(q, 1) * comb(3, 3)
    if q >= 2:
        res += comb(q, 2) * comb(2, 1) * comb(3, 2)
    if q >= 3:
        res += comb(q, 3) * comb(3, 1) * comb(2, 1)
    return res

n, k = map(int, sys.stdin.readline().split())

def main():
    cnt1 = n // k
    res = count(cnt1)
    if k & 1:
        return res
    else:
        if n - k * cnt1 < k // 2:
            res *= 2
        else:
            cnt2 = cnt1 + 1
            res += count(cnt2)
        return res

if __name__ == '__main__':
    ans = main()
    print(ans)
