import sys
from bisect import bisect_left as bi_l
from collections import defaultdict

def main():
    s, t = sys.stdin.read().split()
    if set(t) - set(s):
        print(-1)
        sys.exit()

    n = len(s)
    s *= 2
    c = defaultdict(list)
    for i in range(n * 2):
        c[s[i]].append(i)

    i = 0
    l = 0 # left_most
    for ch in t:
        b = c[ch][bi_l(c[ch], l)]
        if b < n:
            l = b + 1
        else:
            l = b - n + 1
            i += n

    print(i+(l-1)+1) # 最初が0のため

if __name__ == '__main__':
    main()
