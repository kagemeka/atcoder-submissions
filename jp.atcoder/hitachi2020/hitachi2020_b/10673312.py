import sys

A, B, M = map(int, sys.stdin.readline().split())
*a, = map(int, sys.stdin.readline().split())
*b, = map(int, sys.stdin.readline().split())
xyc = zip(*[map(int, sys.stdin.read().split())] * 3)

def main():
    res = min(a) + min(b)

    for x, y, c in xyc:
        res = min(res, a[x-1] + b[y-1] - c)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
