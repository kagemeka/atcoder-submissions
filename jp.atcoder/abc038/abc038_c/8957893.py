import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    cnt = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            cnt += 1
        else:
            res += (1 + cnt) * cnt // 2
            cnt = 1
    res += (1 + cnt) * cnt // 2
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
