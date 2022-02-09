import sys

def count(n, b):
    res = 0
    while n:
        n, r = divmod(n, b)
        res += r
    return res

n = int(sys.stdin.readline().rstrip())

def main():
    res = float('inf')
    for i in range(n + 1):
        res = min(res, count(i, 6) + count(n - i, 9))
    print(res)

if __name__ ==  '__main__':
    main()
