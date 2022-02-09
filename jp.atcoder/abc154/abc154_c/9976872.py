import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    return 'YES' if len(set(a)) == n else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
