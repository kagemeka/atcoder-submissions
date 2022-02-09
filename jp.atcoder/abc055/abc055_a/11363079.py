import sys

n = int(sys.stdin.readline().rstrip())

def main():
    x = 800 * n
    y = 200 * (n // 15)
    print(x - y)

if __name__ ==  '__main__':
    main()
