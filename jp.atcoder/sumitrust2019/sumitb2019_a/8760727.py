import sys

def main():
    m1, d1, m2, d2 = map(int, sys.stdin.read().split())
    if m1 == m2:
        ans = 0
    else:
        ans = 1
    print(ans)

if __name__ == '__main__':
    main()
