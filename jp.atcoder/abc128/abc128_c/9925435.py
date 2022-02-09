import sys

n, m = map(int, sys.stdin.readline().split())
s = [set(map(int, sys.stdin.readline().split()[1:])) for _ in range(m)]
*p, = map(int, sys.stdin.readline().split())

def main():
    combs = 0
    for i in range(2 ** n):
        t = set([j + 1 for j in range(n) if i >> j & 1])
        for k in range(m):
            if len(s[k] & t) & 1 != p[k]:
                break
        else:
            combs += 1

    return combs

if __name__ == '__main__':
    ans = main()
    print(ans)
