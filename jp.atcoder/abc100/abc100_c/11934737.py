import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    for x in a:
        while x % 2 == 0:
            res += 1
            x //= 2
    print(res)

if __name__ ==  '__main__':
    main()
