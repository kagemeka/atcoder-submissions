import sys

*x, k = map(int, sys.stdin.read().split())
x.sort()

def main():
    ans = 'Yay!' if x[-1] - x[0] <= k else ':('
    print(ans)

if __name__ ==  '__main__':
    main()
