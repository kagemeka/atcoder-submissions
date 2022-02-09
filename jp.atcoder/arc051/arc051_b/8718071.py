import sys

def verse_gcd(a, b, k):
    cnt = 0
    while cnt <= k:
        a, b = a + b, a
        cnt += 1
    return a, b

def main():
    k = int(sys.stdin.readline().rstrip())

    a, b = verse_gcd(1, 0, k)
    print(a, b)

if __name__ == '__main__':
    main()
