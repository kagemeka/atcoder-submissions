import sys
from math import floor, sqrt
from bisect import bisect_right as bi_r

def prime_nums(n):
    sieve = set(range(2, n + 1))
    non_prime = set(range(2 * 2, n + 1, 2))
    sieve -= non_prime
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if i in sieve:
            non_prime = set(range(i * 2, n + 1, i))
            sieve -= non_prime
    return sieve

n = int(sys.stdin.readline().rstrip())
ps = prime_nums(n)
ps -= set([2])
ps = sorted(ps)

def main():
    l = len(ps)
    cnt = 0

    # p**4
    for i in range(1, l+1):
        p = ps[i-1]
        if p ** 7 <= n:
            cnt += 1
        else:
            break

    # p**3 * q
    for i in range(1, l+1):
        p = ps[i-1]
        j = bi_r(ps, n // p ** 3)
        if j >= i:
            cnt += j - 1
        elif j > 0:
            cnt += j
        else:
            break

    # p * q * r
    for i in range(1, l-1):
        p = ps[i-1]
        for j in range(i+1, l):
            q = ps[j-1]
            if p * q > n:
                break
            for k in range(j+1, l+1):
                r = ps[k-1]
                if p * q * r > n:
                    break
                cnt += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
