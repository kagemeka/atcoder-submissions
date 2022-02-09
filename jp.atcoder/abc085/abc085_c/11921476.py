import sys

n, y = map(int, sys.stdin.readline().split())
y //= 1000; y -= n

def main():
    for i in range(n + 1):
        if 9 * i > y: break
        if (y - 9 * i) % 4: continue
        j = (y - 9 * i) // 4
        if (i + j > n): continue
        k = n - i - j
        print(i, j, k)
        return
    print(-1, -1, -1)

if __name__ ==  '__main__':
    main()
