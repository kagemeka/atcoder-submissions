import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

def main():
    return s[:k-1] + s[k-1].lower() + s[k:]

if __name__ == '__main__':
    ans = main()
    print(ans)
