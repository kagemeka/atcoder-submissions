import sys

a, b, h = map(int, sys.stdin.read().split())

def main():
    s = (a + b) * h // 2
    print(s)

if __name__ ==  '__main__':
    main()
