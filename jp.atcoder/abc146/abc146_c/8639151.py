# import sys

# a, b, x = map(int, sys.stdin.readline().split())

# def cost(n):
#     return a * n + b * len(str(n))

# if cost(1) > x:
#     print(0)
#     sys.exit()
# elif cost(10 ** 9) <= x:
#     print(10 ** 9)
#     sys.exit()

# l, r = 1, 10 ** 9
# while l <= r:
#     m = (l + r) // 2
#     if cost(m) <= x:
#         l = m + 1
#     else:
#         r = m - 1

# print(r)

import sys

def main():
    A, B, X = map(int, sys.stdin.readline().split())
    # binary search

    def cost(n):
        return A * n + B * len(str(n))

    l = 1; r = 10 ** 9
    while l <= r:
        mid = (l + r) // 2
        if cost(mid) <= X:
            l = mid + 1
        else:
            l = mid - 1

    print(r)

if __name__ == '__main__':
    main()
