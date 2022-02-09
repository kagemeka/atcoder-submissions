import sys

n = int(sys.stdin.readline().rstrip())

def main():
    a = (n + 1) // 2
    ans = a / n
    print(ans)

if __name__ ==  '__main__':
    main()
