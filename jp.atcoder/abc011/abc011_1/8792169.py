import sys

n = int(sys.stdin.readline().rstrip())

def main():
    if n == 12:
        ans = 1
    else:
        ans = n + 1

    print(ans)

if __name__ == '__main__':
    main()
