import sys

def sum_bincount(n):
    l = 0
    r = n
    res = [0] * (41)
    if n < 0:
        return res
    for i in range(40, -1, -1):
        stand = n >> i & 1
        res[i] += 2 ** i * l
        if stand:
            r -= 2 ** i
            res[i] += r + 1
        l = (l << 1) + (stand & 1)
    return res

a, b = map(int, sys.stdin.readline().split())

def main():
    s_a_bin = sum_bincount(a-1)
    s_b_bin = sum_bincount(b)
    res = 0
    for i in range(40, -1, -1):
        res += 2 ** i * ((s_a_bin[i] % 2) ^ (s_b_bin[i] % 2))
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
