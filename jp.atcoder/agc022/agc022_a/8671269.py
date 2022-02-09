# 2019-11-27 15:57:35(JST)
import sys
from string import ascii_lowercase as alphabet
from bisect import bisect_left as bi_l

def main():
    s = sys.stdin.readline().rstrip()
    n = len(s)
    used = set(s)
    not_used = sorted(set(alphabet) - used)

    if not_used:
        ans = s +  not_used[0]
    else:
        cand = []
        for i in range(n-1, 0, -1):
            cand.append(s[i])
            if s[i-1] > s[i]:
                continue
            else:
                ans = s[:i-1] + cand[bi_l(cand, s[i-1])]
                break
        else:
            ans = -1

    print(ans)

if __name__ == '__main__':
    main()
