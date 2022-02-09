import sys

*c, = map(int, sys.stdin.readline().split())

def main():
    print(len(set(c)))

if __name__ ==  '__main__':
    main()
