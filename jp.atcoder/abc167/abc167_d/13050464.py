import sys

n, k, *a = map(int, sys.stdin.read().split())
for i in range(n):
    a[i] -= 1

def main():
    r = k
    cnt = [None] * n
    cnt[0] = 0
    now = 0
    for i in range(1, n + 1):
        now = a[now]
        if cnt[now] is not None:
            r -= cnt[now]
            loop = i - cnt[now]
            break
        cnt[now] = i
    r %= loop
    for _ in range(r):
        now = a[now]
    print(now + 1)

if __name__ == '__main__':
    main()
