# 2019-11-23 18:41:55(JST)
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    ans = (n + 1) % 12 if (n + 1) % 12 != 0 else 12
    print(ans)

if __name__ == '__main__':
    main()
