import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    res = 0
    c = n // k
    res += c ** 3
    if k & 1:
        return res
    if n - k * c < k // 2:
        return res * 2
    else:
        return res + (c + 1) ** 3

if __name__ == '__main__':
    ans = main()
    print(ans)
