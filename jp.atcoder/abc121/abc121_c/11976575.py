import sys

n, m, *ab = map(int, sys.stdin.read().split())
ab = sorted(zip(*[iter(ab)] * 2))

def main():
    res = 0
    cnt = 0
    for a, b in ab:
        if cnt + b >= m:
            res += a * (m - cnt)
            print(res)
            return
        res += a * b
        cnt += b

if __name__ ==  '__main__':
    main()
