import sys

n, y = map(int, sys.stdin.readline().split())
y //= 1000

def main():
    for i in range(n + 1):
        if 10 * i > y: break
        for j in range(n - i + 1):
            k = n - i - j
            if 10 * i + 5 * j + k == y:
                print(i, j, k)
                return
    print(-1, -1, -1)


if __name__ ==  '__main__':
    main()
