import sys

def main():
    n, *a = map(int, sys.stdin.read().split())
    res = 1
    for x in a:
        res *= x
        if res > 10**18:
            print(-1)
            return
    print(res)
if __name__ == '__main__':
    main()
