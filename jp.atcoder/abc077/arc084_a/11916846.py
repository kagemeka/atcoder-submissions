import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r

n = int(sys.stdin.readline().rstrip())
a = sorted(map(int, sys.stdin.readline().split()))
b = sorted(map(int, sys.stdin.readline().split()))
c = sorted(map(int, sys.stdin.readline().split()))

def main():
    combs = 0
    for x in b:
        combs += bi_l(a, x) * (n - bi_r(c, x))
    print(combs)

if __name__ ==  '__main__':
    main()
