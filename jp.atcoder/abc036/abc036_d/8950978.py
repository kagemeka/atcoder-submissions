import sys

MOD = 10 ** 9 + 7

n = int(sys.stdin.readline().rstrip())
ab = map(int, sys.stdin.read().split())
ab = list(zip(ab, ab))

G = [[] for _ in range(n+1)]
for a, b in ab:
    G[a].append(b)
    G[b].append(a)

def main():
    rank = [set() for _ in range(n)]
    stack = [(1, 0)]
    childs = [set() for _ in range(n+1)]
    while stack:
        i, r = stack.pop()
        rank[r].add(i)
        for j in G[i]:
            if i in childs[j]:
                continue
            childs[i].add(j)
            stack.append((j, r + 1))

    res = [None] * (n + 1)
    for r in rank[::-1]:
        for i in r:
            w, b = 1, 1
            for j in childs[i]:
                w *= sum(res[j])
                b *= res[j][0]
                w %= MOD
                b %= MOD
            res[i] = (w, b)

    ans = sum(res[1]) % MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
