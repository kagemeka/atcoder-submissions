import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    ans = c // min(a, b)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
