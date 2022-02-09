import sys

def reverse_gcd(a, b, k):
    cnt = 0
    while cnt <= k:
        a, b = a + b, a
        cnt += 1
    return a, b

def main():
    k = int(sys.stdin.readline().rstrip())
    print(reverse_gcd(1, 0, k))

if __name__ == '__main__':
    main()
