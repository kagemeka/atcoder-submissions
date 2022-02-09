import sys

x = sys.stdin.readline().rstrip()

def main():
    ans = sum(map(int, list(x)))
    print(ans)

if __name__ ==  '__main__':
    main()
