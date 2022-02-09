import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = [None] * n
    x = (sum(a[::2]) - sum(a[1::2])) // 2
    for i in range(n):
        res[i] = x * 2
        x = a[i] - x

    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
