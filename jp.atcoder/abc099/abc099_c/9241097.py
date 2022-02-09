import sys
from math import log, floor

n = int(sys.stdin.readline().rstrip())

def main():
    possible = set([0])
    cnt = 0
    while True:
        nex = set()
        for i in possible:
            for j in range(floor(log(n-i, 6)) + 1):
                nex.add(i + 6 ** j)
            for j in range(floor(log(n-i, 9)) + 1):
                nex.add(i + 9 ** j)
        possible = nex
        cnt += 1
        if n in possible:
            return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
