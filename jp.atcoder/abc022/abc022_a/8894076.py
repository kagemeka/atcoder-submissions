import sys

n, s, t, *a = map(int, sys.stdin.read().split())

def main():
    w = a[0]
    cnt = 0
    if s <= w <= t:
        cnt += 1
    for i in range(1, n):
        w += a[i]
        if s <= w <= t:
            cnt += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
