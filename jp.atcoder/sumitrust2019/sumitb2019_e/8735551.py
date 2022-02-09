import sys

MOD = 10 ** 9 + 7

def main():
    n, *a = map(int, sys.stdin.read().split())

    res = 1
    rgb = [0, 0, 0]
    for i in range(n):
        cur = a[i]
        c = rgb.count(cur)
        res = res * c % MOD
        if cur == rgb[0]:
            rgb[0] += 1
        elif cur == rgb[1]:
            rgb[1] += 1
        elif cur == rgb[2]:
            rgb[2] += 1
    print(res)

if __name__ == '__main__':
    main()
