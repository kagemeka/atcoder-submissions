import sys

n = int(sys.stdin.readline().rstrip())
*a, = map(int, sys.stdin.readline().split())
*b, = map(int, sys.stdin.readline().split())

def attack(i, j, cnt):
    if b[i] <= a[j]:
        a[j] -= b[i]
        cnt += b[i]
        b[i] = 0
    else:
        b[i] -= a[j]
        cnt += a[j]
        a[j] = 0
    return cnt

def main():
    cnt = 0
    for i in range(n):
        cnt = attack(i, i, cnt)
        cnt = attack(i, i+1, cnt)
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
