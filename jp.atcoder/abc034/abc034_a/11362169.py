import sys

x, y = map(int, sys.stdin.readline().split())

def main():
    ans = 'Better' if y > x else 'Worse'
    print(ans)

if __name__ ==  '__main__':
    main()
