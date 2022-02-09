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
    return burger, patty

burger, patty = make_burger(50)

def patty_cnt(l, r, res):
    if l == 0:
        return res + 1
    half_burger = burger[l] // 2 + 1
    half_patty = patty[l] // 2 + 1
    if r == 1:
        return res
    elif r < half_burger:
        return patty_cnt(l-1, r-1, res)
    elif r == half_burger:
        return res + half_patty
    elif r < burger[l]:
        return patty_cnt(l-1, r-half_burger, res+half_patty)
    elif r == burger[l]:
        return res + patty[l]

n, x = map(int, sys.stdin.readline().split())

def main():
    return patty_cnt(n, x, 0)

if __name__ == '__main__':
    ans = main()
    print(ans)
