import sys

n, k, *l = map(int, sys.stdin.read().split())

def main():
    l.sort(reverse=True)
    return sum(l[:k])

if __name__ == '__main__':
    ans = main()
    print(ans)
