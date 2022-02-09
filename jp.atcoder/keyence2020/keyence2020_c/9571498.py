import sys

n, k, s = map(int, sys.stdin.readline().split())

def main():
    m = 10 ** 9
    a = [None] * n
    for i in range(k):
        a[i] = s
    for i in range(k, n):
        if s < m:
            a[i] = m
        else:
            a[i] = 1
    return a

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
