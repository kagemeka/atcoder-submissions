import sys

h, w = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().rstrip() for _ in range(h)]

def main():
    res = [list(s) for s in grid if '#' in s]
    res2 = []
    for j in range(w):
        t = [s[j] for s in res]
        if '#' in t:
            res2.append(t)

    for j in range(len(res)):
        yield ''.join([s[j] for s in res2])

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
