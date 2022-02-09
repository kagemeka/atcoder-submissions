import sys
from math import floor, sqrt

def prime_nums(n):
    sieve = set(range(2, n + 1))
    non_prime = set(range(2 * 2, n + 1, 2))
    sieve -= non_prime
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if i in sieve:
            non_prime = set(range(i * 2, n + 1, i))
            sieve -= non_prime
    return sieve

p = prime_nums(10**5)

cnt = [None] * (10**5+1)
cnt[0] = 0
for i in range(1, 10**5+1, 2):
    if i in p and (i + 1) // 2 in p:
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]
    cnt[i+1] = cnt[i]

q = int(sys.stdin.readline().rstrip())
lr = zip(*[map(int, sys.stdin.read().split())] * 2)

def main():
    for l, r in lr:
        yield cnt[r] - cnt[l-1]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
