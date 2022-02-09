import sys

*x, k = map(int, sys.stdin.read().split())

def main():
    x.sort()
    return 'Yay!' if x[-1] - x[0] <= k else ':('

if __name__ == '__main__':
    ans = main()
    print(ans)
