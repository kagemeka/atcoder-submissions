import sys

n = int(sys.stdin.readline().rstrip())

def simulate(flag):
    cnt = 0
    x = 1
    while x <= n:
        if (cnt & 1) ^ flag:
            x *= 2
        else:
            x = x * 2 + 1
        cnt += 1
    return 'Aoki' if cnt & 1 else 'Takahashi'

def main():
    rank = 0
    m = n
    while m > 1:
        m //= 2
        rank += 1
    print(simulate(rank & 1))

if __name__ == '__main__':
    main()
