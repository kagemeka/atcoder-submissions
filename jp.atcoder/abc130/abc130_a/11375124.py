import sys

x, a = map(int, sys.stdin.readline().split())

def main():
    print(0 if x < a else 10)

if __name__ ==  '__main__':
    main()
