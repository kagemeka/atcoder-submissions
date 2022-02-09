# 2019-11-27 14:53:01(JST)
import sys
def main():
    n, m = map(int, sys.stdin.readline().split())
    if m != 1:
        ans = 1
    else:
        ans = 2
    print(ans)

if __name__ == '__main__':
    main()
