import sys

x = sys.stdin.readline().rstrip()

def main():
    ans = ord(x) - ord('A') + 1
    print(ans)

if __name__ == '__main__':
    main()
