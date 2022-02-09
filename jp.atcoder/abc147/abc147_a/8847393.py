import sys

a = map(int, sys.stdin.readline().split())

def main():
    s = sum(a)
    if s >= 22:
        return 'bust'
    return 'win'

if __name__ == '__main__':
    ans = main()
    print(ans)
