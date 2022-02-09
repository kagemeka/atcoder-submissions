import sys
from math import floor, sqrt, log

x = int(sys.stdin.readline().rstrip())

def main():
    res = [1]
    for b in range(2, x+1):
        p_max = floor(log(x, b))
        if p_max == 1:
            break
        res.append(b ** p_max)
    return max(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
