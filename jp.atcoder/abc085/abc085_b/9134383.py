import sys

n, *d = map(int, sys.stdin.read().split())

def main():
    return len(set(d))

if __name__ == '__main__':
    ans = main()
    print(ans)
