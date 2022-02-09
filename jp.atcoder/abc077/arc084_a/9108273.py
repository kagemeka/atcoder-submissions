import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r

n = int(sys.stdin.readline().rstrip())
*a, = map(int, sys.stdin.readline().split())
*b, = map(int, sys.stdin.readline().split())
*c, = map(int, sys.stdin.readline().split())

def main():
    a.sort()
    b.sort()
    c.sort()
    res = 0
    for i in b:
        cnt_a = bi_l(a, i)
        cnt_c = n - bi_r(c, i)
        res += cnt_a * cnt_c

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
