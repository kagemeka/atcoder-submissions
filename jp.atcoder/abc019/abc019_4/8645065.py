# 2019-11-25 12:34:24(JST)
import sys

def dist(u, v):
    print('? {0} {1}'.format(u, v),flush=True)
    return int(sys.stdin.readline().rstrip())

def main():
    n = int(sys.stdin.readline().rstrip())

    # root = 1 とする
    diameter = 0
    for i in range(2, n+1):
        d = dist(1, i)
        if d > diameter:
            v, diameter = i, d

    for i in range(2, n+1):
        if i != v:
            diameter = max(diameter, dist(v, i))

    print('! {0}'.format(diameter))

if __name__ == '__main__':
    main()
