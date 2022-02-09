import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    c1 = n // k
    c2 = n // (k // 2)
    if (k & 1): cnt = pow(c1, 3)
    else: cnt = pow(c1, 3) + pow(c2 - c1, 3)
    print(cnt)

if __name__ ==  '__main__':
    main()
