import sys

n, m, *sc = map(int, sys.stdin.read().split())
sc = zip(*[iter(sc)] * 2)

def main():
    res = [0] * n
    determined = set()

    for s, c in sc:
        if s in determined:
            return -1
        else:
            res[s-1] = c
            determined.add(s)

    if not res[0]:
        return -1

    res = ''.join([str(d) for d in res])
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
