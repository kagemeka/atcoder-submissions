import sys

def choose2(x):
    return x * (n - 1) // 2

n, m = map(int, sys.stdin.readline().split())

def main():
    res = choose2(n) + choose2(m)
    print(res)

if __name__ ==  '__main__':
    main()
