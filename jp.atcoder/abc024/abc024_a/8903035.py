import sys

a, b, c, k, s, t = map(int, sys.stdin.read().split())

def main():
    fee = a * s + b * t
    if s + t >= k:
        fee = max(0, fee - c * (s + t))

    return fee

if __name__ == '__main__':
    ans = main()
    print(ans)
