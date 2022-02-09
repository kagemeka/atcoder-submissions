import sys
from math import pi

n, *r = map(int, sys.stdin.read().split())
r.sort()

def main():
    s = [None] * n
    inside = 0
    for i in range(n):
        outside = r[i] ** 2 * pi
        s[i] = outside - inside
        inside = outside

    ans = sum(s[n-1::-2])
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
