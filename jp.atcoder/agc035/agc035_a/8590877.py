# 2019-11-24 00:33:09(JST)
import sys

def main():
    n, *a = map(int, sys.stdin.read().split())
    a.sort()
    for i in range(1, n-1):
        if a[i+1] >= a[i] * 2:
            ans = 'No'
            break
    else:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()
