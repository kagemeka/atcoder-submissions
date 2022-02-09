import sys

n, *x = map(int, sys.stdin.read().split())

def main():
    y = sorted(x)
    r = y[n // 2]
    l = y[n // 2 - 1]

    for i in range(n):
        if x[i] <= l:
            yield r
        else:
            yield l

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
