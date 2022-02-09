import sys

group = [None, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

x, y = map(int, sys.stdin.readline().split())

def main():
    ans = 'Yes' if group[x] == group[y] else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
