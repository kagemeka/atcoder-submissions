import sys
from math import floor, sqrt, log

x = int(sys.stdin.readline().rstrip())

def main():
    b_max = floor(sqrt(x))
    res = [1]
    for b in range(2, b_max + 1):
        p_max = floor(log(x, b))
        res.append(b ** p_max)
    return max(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
