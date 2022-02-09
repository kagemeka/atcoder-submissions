import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    for s in [int(x) for x in sys.stdin.readline().split()][1:]:
        graph[s-1].append(i)
*p, = map(int, sys.stdin.readline().split())

def main():
    cnt = 0
    for i in range(1 << n):
        bits = [0] * m
        for j in range(n):
            if i >> j & 1:
                for s in graph[j]:
                    bits[s] ^= 1
        for j in range(m):
            if bits[j] ^ p[j]: break
        else:
            cnt += 1
    print(cnt)

if __name__ ==  '__main__':
    main()
