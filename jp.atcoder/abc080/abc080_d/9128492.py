import sys

inf = float('inf')

n, C, *stc = map(int, sys.stdin.read().split())
stc = list(zip(*[iter(stc)] * 3))

def main():
    res = [(-0.5, None) for _ in range(C)] # C台あれば確実に足りる
    stc.sort()

    for s, t, c in stc:
        c -= 1
        interval = inf
        for i in range(C):
            last, prev = res[i]
            if prev != c:
                last += 0.5

            if last <= s:
                if s - last < interval:
                    interval = s - last
                    to_use = i
        res[to_use] = (t, c)

    ans = 0
    for i in range(C):
        if res[i][0] != -0.5:
            ans += 1
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
