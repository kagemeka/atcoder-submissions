import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    ans = k * (k - 1)**(n-1)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
