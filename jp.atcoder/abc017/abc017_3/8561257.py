# 2019-11-22 22:30:40(JST)
import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    lrs = map(int, sys.stdin.read().split())
    *lrs, = zip(lrs, lrs, lrs)

    total = sum(s for l, r, s in lrs)
    res = [total for _ in range(m+1)]
    res[0] = 0
    # res[i]: 宝石iを取らない場合の最大値

    for i in range(1, m+1):
        # 宝石iが入っているかどうか
        for l, r, s in lrs:
            if l <= i <= r:
                res[i] -= s

    ans = max(res)
    print(ans)

if __name__ == '__main__':
    main()
