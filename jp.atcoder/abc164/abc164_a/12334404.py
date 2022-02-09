import sys

s, w = map(int, sys.stdin.readline().split())

def main():
    ans = 'unsafe' if w >= s else 'safe'
    print(ans)

if __name__ == '__main__':
    main()
