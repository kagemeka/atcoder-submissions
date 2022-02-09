import sys
from string import digits
from itertools import product
from bisect import bisect_left as bi_l

n, k, *dislikes = sys.stdin.read().split()

def main():
    likes = sorted(set(digits) - set(dislikes))
    cand = product(likes, repeat=len(n))
    *cand, = map(lambda x: int(''.join(x)), cand)
    cand.sort()
    res = bi_l(cand, int(n))
    if res < len(likes) ** len(n):
        return cand[res]

    if likes[0] == '0':
        ans = likes[1] + '0' * len(n)
    else:
        ans = likes[0] * (len(n)+1)
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
