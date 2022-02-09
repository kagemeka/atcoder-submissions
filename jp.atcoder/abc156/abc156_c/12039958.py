import sys

n, *x = map(int, sys.stdin.read().split())

def main():
    p = round(sum(x) / n)
    res = sum([(p - i) ** 2 for i in x])
    print(res)

if __name__ ==  '__main__':
    main()
