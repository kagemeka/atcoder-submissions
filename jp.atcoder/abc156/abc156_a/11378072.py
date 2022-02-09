import sys

n, r = map(int, sys.stdin.readline().split())

def main():
    i = r + 100 * (10 - n)
    print(i)

if __name__ ==  '__main__':
    main()
