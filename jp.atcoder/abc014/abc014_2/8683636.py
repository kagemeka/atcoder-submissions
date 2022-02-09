import sys
def main():
    n, x, *a = map(int, sys.stdin.read().split())

    s = 0
    for i in range(n):
        if x>>i & 1:
            s += a[i]

    print(s)

if __name__ == '__main__':
    main()
