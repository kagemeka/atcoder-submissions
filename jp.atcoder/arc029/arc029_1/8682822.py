# 2019-11-28 15:32:26(JST)
import sys
def main():
    n, *t = map(int, sys.stdin.read().split())
    t.sort()
    if n == 1:
        ans = t[0]
    if n == 2:
        ans = t[1]
    if n == 3:
        ans = max(sum(t[:2]), t[2])
    elif n == 4:
        if t[3] >= sum(t[:3]):
            ans = t[3]
        else:
            ans = max(t[0] + t[3], sum(t[1:3]))

    print(ans)

if __name__ == '__main__':
    main()
