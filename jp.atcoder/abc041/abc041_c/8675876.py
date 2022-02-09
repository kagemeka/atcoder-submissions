# 2019-11-27 22:34:20(JST)
import sys
def main():
    n, *a = map(int, sys.stdin.read().split())
    a = sorted(list(enumerate(a, 1)), key=lambda x: x[1], reverse=True)
    for i in range(n):
        print(a[i][0])

if __name__ == '__main__':
    main()
