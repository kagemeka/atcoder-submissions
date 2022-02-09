import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    s = n
    c = m
    res = 0
    if c < 2 * s:
        return m // 2

    res += s
    c -= 2 * s
    res += c // 4
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
