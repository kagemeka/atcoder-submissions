import sys

def main():
    a, b = map(float, sys.stdin.readline().split())
    a = int(a)
    b = int(b * 100)
    c = a * b
    print(c // 100)
if __name__ == '__main__':
    main()
