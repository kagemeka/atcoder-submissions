import sys

MOD = 10 ** 9 + 7

h, w, k = map(int, sys.stdin.readline().split())

def main():
    ok = []
    for i in range(2 ** (w - 1)):
        prev = False
        for j in range(w-1):
            if i >> j & 1:
                if prev:
                    break
                else:
                    prev = True
            else:
                prev = False
        else:
            ok.append(i)

    lcr = [(letter, 0) for letter in 'lcr']
    a = [dict(lcr) for _ in range(w)]
    for i in ok:
        j = 0
        while j < w:
            if i >> j & 1:
                a[j]['r'] += 1
                a[j+1]['l'] += 1
                j += 2
            else:
                a[j]['c'] += 1
                j += 1

    res = [0] * w
    res[0] = 1
    for _ in range(h):
        nex = [0] * w
        for j in range(w):
            if j == 0:
                nex[j] = res[j] * a[j]['c'] + res[j+1] * a[j]['r']
            elif j < w - 1:
                nex[j] = res[j-1] * a[j]['l'] + res[j] * a[j]['c'] + res[j+1] * a[j]['r']
            else:
                nex[j] = res[j-1] * a[j]['l'] + res[j] * a[j]['c']
        for j in range(w):
            nex[j] %= MOD
        res = nex

    return res[k-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
