import sys
import scipy.misc

def comb(n, r):
    return scipy.misc.comb(n, r, exact=True)

n, k = map(int, sys.stdin.readline().split())

def main():
    res = 0
    res += comb(3, 1) * comb(2, 1) * ((k - 1) / n) * (1 / n) * ((n - k) / n)
    res += comb(3, 2) * (1 / n) ** 2 * ((n - 1) / n)
    res += comb(3, 3) * (1 / n) ** 3
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
