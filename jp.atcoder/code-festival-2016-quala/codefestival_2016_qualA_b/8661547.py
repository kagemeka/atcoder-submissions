# 2019-11-26 17:11:55(JST)
import sys
def main():
    n, *a = map(int, sys.stdin.read().split())
    a = [None] + a

    cnt = 0
    for i in range(1, n):
        j = a[i]
        if j > i and a[j] == i:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
