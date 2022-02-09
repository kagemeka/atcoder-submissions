import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    res = a + b
    print('error' if res >= 10 else res)

if __name__ ==  '__main__':
    main()
