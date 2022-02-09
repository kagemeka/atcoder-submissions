import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    print(int(round(a + b) / 2))

if __name__ ==  '__main__':
    main()
