import sys
from math import floor, sqrt, log

x = int(sys.stdin.readline().rstrip())

def main():
    res = [1]
    for b in range(2, x+1):
        p = 2
        while b ** p <= x:
            res.append(b ** p)
            p += 1
    return max(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
