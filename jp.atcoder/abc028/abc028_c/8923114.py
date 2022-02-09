import sys

a, b, c, d, e = map(int, sys.stdin.readline().split())

def main():
    ans = max(a + d + e, b + c + e)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
