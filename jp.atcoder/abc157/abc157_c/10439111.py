import sys

n, m, *sc = map(int, sys.stdin.read().split())
sc = zip(*[iter(sc)] * 2)

def main():
    res = [0] * n

    for s, c in sc:
        if res[s-1]:
            if res[s-1] != c:
                return -1
        else:
            res[s-1] = c

    if not res[0]:
        return -1
    res = ''.join([str(d) for d in res])
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
