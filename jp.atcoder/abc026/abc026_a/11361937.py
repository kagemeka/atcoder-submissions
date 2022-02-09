import sys

a = int(sys.stdin.readline().rstrip())

def main():
    x = a // 2
    y = a - x
    print(x * y)

if __name__ ==  '__main__':
    main()
