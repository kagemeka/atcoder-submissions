import sys
def main():
    x, y = map(int, sys.stdin.readline().split())
    print(max(x, y))

if __name__ == '__main__':
    main()
