import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    l = m * 360 / 60
    s = n * 360 / 12 + l / 12
    d = abs(l - s) % 360
    ans = min(d, 360 - d)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
