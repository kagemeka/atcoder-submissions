import sys

g = [None, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

x, y = map(int, sys.stdin.readline().split())

def main():
    return 'Yes' if g[x] == g[y] else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
