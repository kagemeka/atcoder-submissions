import sys

*a, = map(int, sys.stdin.readline().split())

def main():
    ans = 'bust' if sum(a) >= 22 else 'win'
    print(ans)

if __name__ ==  '__main__':
    main()
