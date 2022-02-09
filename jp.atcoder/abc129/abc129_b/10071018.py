import sys

n, *W = map(int, sys.stdin.read().split())

def main():
    s1 = 0
    s2 = sum(W)
    res = s2
    for w in W:
        s1 += w
        s2 -= w
        res = min(res, abs(s2 - s1))

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
