# 2019-11-24 00:33:09(JST)
import sys
import collections

def main():
    n, *a = map(int, sys.stdin.read().split())

    c = collections.Counter(a)

    ans = 'No'
    # if len(c) == 2 and 0 in c and c[0] == n / 3:
    #     ans = 'Yes'
    # elif len(c) == 3 and not 0 in c:
    #     for i in c.values():
    #         if i != n / 3:
    #             break
    #     else:
    #         ans = 'Yes'
    # elif 0 in c and c[0] == n:
    #     ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    main()
