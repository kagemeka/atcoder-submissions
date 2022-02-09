import sys
from itertools import combinations, product
from string import digits
from collections import Counter

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    # t = [None] * (n+1)
    # c = Counter(s)
    # t[0] = set(s)
    # # for i in range(n):
    # #     c[s[i]] -= 1
    # #     if c[s[i]] == 0:
    # #         t[i+1] = t[i] - set([s[i]])
    # #     else:
    # #         t[i+1] = t[i]
    # # print(t)



    cand = list(''.join(p) for p in product(digits, repeat=3))
    # print(cand)
    # for comb in combinations(s, 3):
    #     res.add(comb)

    # ans = len(res)
    # print(ans)

    res = set()
    for c in cand:
        i = s.find(c[0])
        if i == -1:
            continue
        j = s.find(c[1], i+1)
        if j == -1:
            continue
        k = s.find(c[2], j+1)
        if k == -1:
            continue

        res.add(c)

    ans = len(res)
    print(ans)

if __name__ == '__main__':
    main()
