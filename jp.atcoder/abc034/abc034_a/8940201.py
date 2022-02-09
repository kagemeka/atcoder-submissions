import sys

x, y = map(int, sys.stdin.readline().split())

def main():
    if y > x:
        return 'Better'
    return 'Worse'

if __name__ == '__main__':
    ans = main()
    print(ans)
