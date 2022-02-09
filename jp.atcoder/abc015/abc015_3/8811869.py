import sys

n, k = map(int, sys.stdin.readline().split())
a = map(int, sys.stdin.read().split())
a = list(zip(*([a] * k)))

def main():
    stack = []
    for y in a[0]:
        stack.append((1, y))

    res = set()
    while stack:
        rank, x = stack.pop()
        if rank == n:
            res.add(x)
            continue
        for y in a[rank]:
            stack.append((rank + 1, x ^ y))

    return 'Found' if 0 in res else 'Nothing'

if __name__ == '__main__':
    ans = main()
    print(ans)
