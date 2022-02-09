import sys
from bisect import bisect_left as bi_l

*I, = map(int, sys.stdin.read().split())
n, m, x, y = I[:4]
a = I[4:4+n]
b = I[4+n:]

def main():
    cnt = 0
    t = 0
    flag = False
    while True:
        if not flag:
            nex = bi_l(a, t)
            if nex == n:
                break
            t = a[nex] + x
            flag = True
        else:
            nex = bi_l(b, t)
            if nex == m:
                break
            t = b[nex] + y
            cnt += 1
            flag = False
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
