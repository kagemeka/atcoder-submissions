import sys

*a, = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yes' if len(set(a)) == 2 else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
