# 2019-11-24 00:33:09(JST)
import sys
import collections

def main():
    n, *a = map(int, sys.stdin.read().split())

    c = collections.Counter(a)

    ans = 'No'
    if 0 in c:
        if c[0] == n:
            ans = 'Yes'
        elif c[0] == n / 3 and len(c) == 2:
            ans = 'Yes'

    else:
        if len(c) == 3:
            for i in c.values():
                if i != n / 3:
                    break
            else:
                b = list(c.keys())
                if b[0] ^ b[1] == b[2]:
                    ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()
