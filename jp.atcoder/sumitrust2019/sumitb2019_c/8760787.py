import sys

def main():
    x = int(sys.stdin.readline().rstrip())
    q, r = divmod(x, 100)

    if 5 * q >= r:
        ans = 1
    else:
        ans = 0

    print(ans)

if __name__ == '__main__':
    main()
