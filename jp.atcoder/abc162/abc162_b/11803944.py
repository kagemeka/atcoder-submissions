import sys

n = int(sys.stdin.readline().rstrip())

def main():
    ans = 0
    for i in range(1, n + 1):
        if (i % 3 == 0) or (i % 5 == 0):
            continue
        ans += i
    print(ans)

if __name__ ==  '__main__':
    main()
