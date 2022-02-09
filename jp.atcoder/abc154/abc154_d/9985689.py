import sys

n, k, *p = map(int, sys.stdin.read().split())

def main():
    ex = [(1 + i) * i // 2  / i for i in p]
    l = 0; r = k

    res = []
    s = sum(ex[l:r])
    res.append(s)
    while r < n:
        s -= ex[l]
        s += ex[r]
        l += 1
        r += 1
        res.append(s)
    return max(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
