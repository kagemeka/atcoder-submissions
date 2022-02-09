import sys

n, *A = map(int, sys.stdin.read().split())

def main():
    prod = 1
    for a in A:
        prod *= a

    numerator = prod
    denominator = 0
    for a in A:
        denominator += prod // a

    return numerator / denominator

if __name__ == '__main__':
    ans = main()
    print(ans)
