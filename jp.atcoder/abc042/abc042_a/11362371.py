import sys

*a, = map(int, sys.stdin.readline().split())

def main():
    a.sort()
    ans = 'YES' if a[0] == a[1] == 5 and a[2] == 7 else 'NO'
    print(ans)

if __name__ ==  '__main__':
    main()
