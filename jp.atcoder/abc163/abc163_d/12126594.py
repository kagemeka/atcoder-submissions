import sys
from itertools import accumulate
MOD = 10 ** 9 + 7


n, k = map(int, sys.stdin.readline().split())

def main():
    a = range(n + 1)
    sl = list(accumulate(a))
    sr = list(accumulate(a[::-1]))

    res = 0
    for i in range(k, n + 2):
        res += sr[i-1] - sl[i-1] + 1
        res %= MOD
    print(res)






if __name__ == '__main__':
    main()
