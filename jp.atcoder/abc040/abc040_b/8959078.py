import sys
from math import floor

n = int(sys.stdin.readline().rstrip())

def main():
    res = 10 ** 6

    for i in range(1, floor(n ** 0.5) + 1):
        j, r = divmod(n, i)
        res = min(res, j - i + r)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
