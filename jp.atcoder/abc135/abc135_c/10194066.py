import sys

n = int(sys.stdin.readline().rstrip())
*a, = map(int, sys.stdin.readline().split())
*b, = map(int, sys.stdin.readline().split())

def main():
    cnt = 0
    for i in range(n):
        if b[i] <= a[i]:
            a[i] -= b[i]
            cnt += b[i]
            b[i] = 0
        else:
            b[i] -= a[i]
            cnt += a[i]
            a[i] = 0

        if b[i] >= a[i+1]:
            cnt += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
        else:
            a[i+1] -= b[i]
            cnt += b[i]
            b[i] = 0
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
