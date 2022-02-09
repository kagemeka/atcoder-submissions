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

    res = [0] * w
    res[0] = 1
    for _ in range(h):
        nex = [0] * w
        for i in ok:
            j = 0
            while j < w:
                if i >> j & 1:
                    nex[j] += res[j+1]
                    nex[j+1] += res[j]
                    j += 2
                else:
                    nex[j] += res[j]
                    j += 1
        for j in range(w):
            nex[j] %= MOD
        res = nex

    return res[k-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
