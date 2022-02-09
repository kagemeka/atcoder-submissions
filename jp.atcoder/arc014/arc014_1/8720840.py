import sys
def main():
    n = int(sys.stdin.readline().rstrip())
    if n % 2 == 0:
        ans = 'BLue'
    else:
        ans = 'Red'
    print(ans)

if __name__ == '__main__':
    main()
