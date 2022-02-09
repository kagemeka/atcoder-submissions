import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    q, r = divmod(sum(a), n)
    if r:
        return -1

    cnt = 0
    connected = 0
    tmp = 0
    for i in range(n):
        if not connected:
            if a[i] != q:
                connected = 1
                tmp = a[i]
                cnt += 1
        else:
            total = tmp + a[i]
            if total == q * (connected + 1):
                connected = 0
                tmp = 0
            else:
                connected += 1
                cnt += 1
                tmp += a[i]

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
