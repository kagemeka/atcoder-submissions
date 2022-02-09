import sys
from math import ceil, log2

n = int(sys.stdin.readline().rstrip())

def main():
    m = ceil(log2(n))
    res = []
    for i in range(m+1):
        if n >> i & 1:
            res.append(2 ** i)

    yield len(res)
    for r in res:
        yield r

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
