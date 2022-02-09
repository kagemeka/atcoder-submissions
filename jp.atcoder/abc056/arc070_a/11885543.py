import sys

x = int(sys.stdin.readline().rstrip())

def main():
    n = int((x * 2) ** 0.5)
    res = n if (1 + n) * n // 2 >= x else n + 1
    print(res)

if __name__ ==  '__main__':
    main()
