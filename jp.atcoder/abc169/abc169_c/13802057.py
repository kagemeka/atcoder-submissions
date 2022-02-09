import sys

def main():
    a, b = map(float, sys.stdin.readline().split())
    c = a * b
    print(int(c))
if __name__ == '__main__':
    main()
