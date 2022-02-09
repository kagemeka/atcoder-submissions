import sys

*a, = map(int, sys.stdin.readline().split())

def main():
    a.sort(reverse=True)
    return a[2]

if __name__ == "__main__":
    ans = main()
    print(ans)
