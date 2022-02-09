import sys

n = int(sys.stdin.readline().rstrip())

def main():
    ans = sum([x for x in range(1, n + 1) if x % 3 and x % 5])
    print(ans)

if __name__ ==  '__main__':
    main()
