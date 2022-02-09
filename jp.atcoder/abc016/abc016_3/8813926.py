import sys

n, m = map(int, sys.stdin.readline().split())
ab = map(int, sys.stdin.read().split())
ab = list(zip(ab, ab))

def main():
    graph = [set() for _ in range(n+1)]
    for a, b in ab:
        graph[a].add(b)
        graph[b].add(a)

    for i in range(1, n+1):
        friends = graph[i]
        f_of_f = set()
        for f in friends:
            f_of_f |= set(graph[f])

        res = f_of_f - friends - set([i])
        yield len(res)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
