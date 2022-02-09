import sys

n, m, *ab = map(int, sys.stdin.read().split())
g = [set() for _ in range(n+1)]
for a, b in zip(*[iter(ab)] * 2):
    g[a].add(b)
    g[b].add(a)

def main():
    return 'POSSIBLE' if g[1] & g[n] else 'IMPOSSIBLE'

if __name__ == '__main__':
    ans = main()
    print(ans)
