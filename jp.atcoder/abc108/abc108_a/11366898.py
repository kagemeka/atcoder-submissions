import sys

k = int(sys.stdin.readline().rstrip())

def main():
    x = k // 2
    y = k - x
    print(x * y)

if __name__ ==  '__main__':
    main()
