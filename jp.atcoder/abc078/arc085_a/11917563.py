import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    res = (1900 * m + 100 * (n - m)) * pow(2, m)
    print(res)

if __name__ ==  '__main__':
    main()
