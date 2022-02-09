import sys

def make_burger(n):
    patty = [None] * (n + 1)
    bun = [None] * (n + 1)
    patty[0] = 1
    bun[0] = 0
    burger = [None] * (n + 1)
    burger[0] = 1
    for i in range(n):
        patty[i+1] = patty[i] * 2 + 1
        bun[i+1] = bun[i] * 2 + 2
        burger[i+1] = patty[i+1] + bun[i+1]

    return patty, bun, burger

n, x = map(int, sys.stdin.readline().split())

def main():
    r = x
    patty, bun, burger = make_burger(n)

    res = 0
    for l in range(n, 0, -1):
        half_burger = burger[l] // 2 + 1
        half_patty = patty[l] // 2 + 1
        if r == 1:
            r = 0
            break
        elif r < half_burger:
            r -= 1
        elif r == half_burger:
            res += half_patty
            r = 0
            break
        elif r < burger[l]:
            res += half_patty
            r -= half_burger
        elif r == burger[l]:
            res += patty[l]
            r = 0
            break
    if r:
        res += 1
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
