import sys

k = int(sys.stdin.readline().rstrip())

def main():
    n = 50
    print(n)
    q, r = divmod(k, n)
    lo = 49 - r + q
    hi = 50 + q

    a = [lo] * (50 - r) + [hi] * r
    return a

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
