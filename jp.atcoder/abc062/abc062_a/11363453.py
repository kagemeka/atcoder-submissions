import sys

group = [None, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]

x, y = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yes' if group[x] == group[y] else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
