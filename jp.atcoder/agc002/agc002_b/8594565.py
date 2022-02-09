# 2019-11-24 12:12:53(JST)
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    xy = map(int, sys.stdin.read().split())
    xy = zip(xy, xy)

    count = dict((i, 1) for i in range(1, n+1))
    may_contain_red = set([1])

    for x, y in xy:
        count[x] -= 1; count[y] += 1
        if x in may_contain_red:
            may_contain_red.add(y)
            if count[x] == 0:
                may_contain_red ^= set([x])

    ans = len(may_contain_red)
    print(ans)

if __name__ == '__main__':
    main()
