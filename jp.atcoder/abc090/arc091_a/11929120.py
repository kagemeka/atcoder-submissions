import sys

n, m = map(int, sys.stdin.readline().split())
if n > m: n, m = m, n

def main():
    res = abs(m - 2) if n == 1 else (n - 2) * (m - 2)
    print(res)

if __name__ ==  '__main__':
    main()
