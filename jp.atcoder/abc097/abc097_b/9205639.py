import sys
from math import floor

x = int(sys.stdin.readline().rstrip())

def main():
    res = [1]
    i = 2
    while x ** (1 / i) >= 2:
        res.append(floor(x ** (1 / i)) ** i)
        i += 1

    return max(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
