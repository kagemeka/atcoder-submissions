import sys

P = 10 ** 9 + 7
A, B, C = map(int, sys.stdin.read().split())

def main():
    upper_r = (B * C % P - A * C % P) % P
    upper_c = (B * C % P - A * B % P) % P
    inv_lower = pow((A * B % P + A * C % P - B * C % P) % P, P - 2, P)

    r = upper_r * inv_lower % P
    c = upper_c * inv_lower % P
    return r, c

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
