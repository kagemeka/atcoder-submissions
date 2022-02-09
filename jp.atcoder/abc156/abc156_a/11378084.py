import sys

n, r = map(int, sys.stdin.readline().split())

def main():
    i = r + 100 * max(10 - n, 0)
    print(i)

if __name__ ==  '__main__':
    main()
