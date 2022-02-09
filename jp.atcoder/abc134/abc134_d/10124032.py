import sys

n, *a = map(int, sys.stdin.read().split())
a = [None] + a

def main():
    res = [0] * (n + 1)
    chosen = []
    for i in range(n, 0, -1):
        tmp = sum(res[i*2:n+1:i]) & 1
        if tmp ^ a[i]:
            res[i] = 1
            chosen.append(i)

    if chosen:
        m = len(chosen)
        return [m], chosen[::-1]
    else:
        return [[0]]

if __name__ == '__main__':
    ans = main()
    for a in ans:
        print(*a, sep=' ')
