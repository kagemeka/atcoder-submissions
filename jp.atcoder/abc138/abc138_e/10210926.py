import sys
from bisect import bisect_left as bi_l
from collections import defaultdict

s, t = sys.stdin.read().split()
l = len(s)
s *= 2

def main():
    for c in t:
        try:
            s.index(c)
        except:
            return -1

    d = defaultdict(list)
    for i in range(l*2):
        d[s[i]].append(i)

    for c in d:
        d[c].sort()

    j = 0
    cnt = 0
    for c in t:
        k = bi_l(d[c], j)
        j = d[c][k]
        if j >= l:
            j -= l
            cnt += 1
        j += 1
    ans = l * cnt + j

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
