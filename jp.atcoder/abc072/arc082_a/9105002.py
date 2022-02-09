import sys
from collections import defaultdict

n, *a = map(int, sys.stdin.read().split())

def main():
    res = defaultdict(int)
    for i in a:
        res[i-1] += 1
        res[i] += 1
        res[i+1] += 1

    return max(res.values())

if __name__ == '__main__':
    ans = main()
    print(ans)
