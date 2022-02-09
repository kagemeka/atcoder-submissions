import sys

n, m, *ab = map(int, sys.stdin.read().split())
g_1 = set()
g_n = set()
for a, b in zip(*[iter(ab)] * 2):
    if a == 1 or b == 1:
        g_1.add(b)
    elif a == n or b == n:
        g_n.add(a)

def main():
    return 'POSSIBLE' if g_1 & g_n else 'IMPOSSIBLE'

if __name__ == '__main__':
    ans = main()
    print(ans)
