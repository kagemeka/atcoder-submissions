import sys
from string import digits

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    place = dict((i, set()) for i in digits)
    for i in range(n):
        place[s[i]].add(i)

    l = [None] * n
    l[0] = set()
    for i in range(1, n):
        l[i] = l[i-1] | set([s[i-1]])

    r = [None] * n
    r[n-1] = set()
    for i in range(n-2, -1, -1):
        r[i] = r[i+1] | set([s[i+1]])

    res = set()
    for j in digits:
        for i in digits:
            for k in digits:
                for c in place[j]:
                    if not i in l[c]:
                        continue
                    if not k in r[c]:
                        continue
                    res.add((i, j, k))
                    break
    print(len(res))


if __name__ == '__main__':
    main()
