# 2019-11-26 14:51:37(JST)
import sys

def main():
    n, m, *a = map(int, sys.stdin.read().split())

    res = []
    latest = set()
    for i in range(m-1, -1, -1):
        if {a[i]} & latest:
            # latestと重複があればlatestではない
            continue
        else:
            latest.add(a[i])
            res.append(a[i])

    ans = res + sorted(set(range(1, n+1)) - set(res))
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()
