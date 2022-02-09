import sys

n, m = map(int, sys.stdin.readline().split())
xy = map(int, sys.stdin.read().split())
xy = zip(xy, xy)
graph = [set() for _ in range(n)]
for x, y in xy:
    graph[x-1].add(y-1)


def main():
    res = [0] * 2**n
    res[0] = 1
    for i in range(1, 2**n):
        partial = set()
        for j in range(n):
            if i >> j & 1:
                partial.add(j)
        for j in partial:
            if not graph[j] & partial:
                res[i] += res[i ^ (2**j)]

    return res[-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
